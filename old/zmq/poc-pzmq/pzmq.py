import functools
import logging

import zmq


logger = logging.getLogger(__name__)


class MethodNotFound(Exception):
    pass


class Method(object):
    def __init__(self, name, input_cls, output_cls, func):
        self.name = name
        self.input_cls = input_cls
        self.output_cls = output_cls
        self.func = func

    def unserialize_input(self, b_data):
        input_ = self.input_cls()
        input_.ParseFromString(b_data)
        return input_

    def serialize_input(self, input_):
        return input_.SerializeToString()

    def unserialize_output(self, b_data):
        output = self.output_cls()
        output.ParseFromString(b_data)
        return output

    def serialize_output(self, output):
        return output.SerializeToString()


class ServiceDefinition(object):
    def __init__(self, name, methods):
        self.name = name
        self.methods = methods

    def get_method(self, method_name):
        try:
            return self.methods[method_name]
        except KeyError:
            raise MethodNotFound()


class Worker(object):
    def __init__(self, service_definition, broker_url, ctx=None):
        self.service_definition = service_definition
        self.ctx = ctx or zmq.Context()
        self.broker_url = broker_url

    def run(self):
        self.socket = self.ctx.socket(zmq.REP)
        self.socket.connect(self.broker_url)
        while True:
            b_method_name, b_input = self.socket.recv_multipart()
            try:
                method_name = b_method_name.decode('utf8')
                method = self.service_definition.get_method(method_name)
                b_output = self.call_method(method, b_input)
                status_code = b'ok'
            except Exception as ex:
                logger.exception("Error when calling %r on service %r", method_name, self.service_definition.name)
                b_output = repr(ex).encode('utf8')
                status_code = b'error'
            self.socket.send_multipart((status_code, b_output))

    def call_method(self, method, b_input):
        input_ = method.unserialize_input(b_input)
        output = method.func(input_)
        b_output = method.serialize_output(output)
        return b_output


class Broker(object):
    def __init__(self, url_clients, url_workers, ctx=None):
        self.ctx = ctx or zmq.Context()
        self.url_clients = url_clients
        self.url_workers = url_workers

    def run(self):
        self.frontend = self.ctx.socket(zmq.ROUTER)
        self.frontend.bind(self.url_clients)
        self.backend = self.ctx.socket(zmq.DEALER)
        self.backend.bind(self.url_workers)

        zmq.device(zmq.QUEUE, self.frontend, self.backend)

        # We never get here...
        self.frontend.close()
        self.backend.close()


class Client(object):
    def __init__(self, service_definition, broker_url, ctx=None):
        self.service_definition = service_definition
        for method_name in self.service_definition.methods:
            setattr(self, method_name, functools.partial(self.call, method_name))

        self.broker_url = broker_url
        self.ctx = ctx or zmq.Context()
        self.socket = self.ctx.socket(zmq.REQ)
        self.socket.connect(broker_url)

    def call(self, method_name, input_):
        method = self.service_definition.get_method(method_name)
        b_input = method.serialize_input(input_)
        self.socket.send_multipart((method_name.encode('utf8'), b_input))
        status_code, b_output = self.socket.recv_multipart()
        if status_code != b'ok':
            raise Exception(b_output.decode('utf8'))
        output = method.unserialize_output(b_output)
        return output
