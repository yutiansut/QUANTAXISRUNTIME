import asyncio
import aiozmq.rpc
import zmq

class ServerHandler(aiozmq.rpc.AttrHandler):

    @aiozmq.rpc.method
    def remote_func(self, a:int, b:int):
        return a + b




def start_zmq_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://%s:%i" % (HOST, PORT))
    obj = rpc_test.SomeRemoteClass()
    try:
        while True:    
            a = socket.recv()
            if a == "giveme":
                socket.send(obj.giveme())
            else:
                socket.send("get %i" % len(a))
    except KeyboardInterrupt:
        exit()


@asyncio.coroutine
def go():
    server = yield from aiozmq.rpc.serve_rpc(
        ServerHandler(), bind='tcp://127.0.0.1:5555')
    client = yield from aiozmq.rpc.connect_rpc(
        connect='tcp://127.0.0.1:5555')

    ret = yield from client.call.remote_func(1, 2)
    assert 3 == ret

    server.close()
    client.close()

asyncio.get_event_loop().run_until_complete(go())