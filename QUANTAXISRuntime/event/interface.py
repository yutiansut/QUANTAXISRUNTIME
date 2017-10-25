#coding:utf-8


import asyncio
from asyncio import BaseProtocol, BaseTransport



class QAR_Transport(BaseTransport):

    def write(self, data):
        raise NotImplementedError

    def abort(self):

        raise NotImplementedError

    def getsockopt(self, option):

        raise NotImplementedError

    def setsockopt(self, option, value):

        raise NotImplementedError

    def set_write_buffer_limits(self, high=None, low=None):

        raise NotImplementedError

    def get_write_buffer_limits(self):
        raise NotImplementedError

    def get_write_buffer_size(self):
        """Return the current size of the write buffer."""
        raise NotImplementedError

    def pause_reading(self):

        raise NotImplementedError

    def resume_reading(self):

        raise NotImplementedError

    def bind(self, endpoint):

        raise NotImplementedError

    def unbind(self, endpoint):

        raise NotImplementedError

    def bindings(self):

        raise NotImplementedError

    def connect(self, endpoint):

        raise NotImplementedError

    def disconnect(self, endpoint):
    
        raise NotImplementedError

    def connections(self):

        raise NotImplementedError

    def subscribe(self, value):

        raise NotImplementedError

    def unsubscribe(self, value):

        raise NotImplementedError

    def subscriptions(self):

        raise NotImplementedError

    @asyncio.coroutine
    def enable_monitor(self, events=None):

        raise NotImplementedError

    def disable_monitor(self):
        """Stop the socket event monitor.
        """
        raise NotImplementedError


class QAR_Protocol(BaseProtocol):


    def msg_received(self, data):
        """

        data is the multipart tuple of bytes with at least one item.
        """

    def event_received(self, event):
        """
        This method is only called when a socket monitor is enabled.

        :param event: A namedtuple containing 3 items `event`, `value`, and
          `endpoint`.
        """
