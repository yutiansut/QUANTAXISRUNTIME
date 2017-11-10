import asyncio


class QAR_BaseProtocol(asyncio.BaseProtocol):
    def connection_made(self,transport):
        """
        called when connection is made
        """
    def connection_lost(self,exc):
        """
        exc is an exception or None
        """
    def pause_writing(self):
        """
        called when buf goes over the high-water mark
        """
    def resume_writing(self):
        """
        called when buf drains over the low-water mark
        """
    
class QAR_Protocol(QAR_BaseProtocol):
    """
     start -> CM [-> DR*/MR*/ER*] [-> ER?] -> CL -> end
    """
    def data_received(self,data):
        """
        called when data is received
        """
    def eof_received(self):
        """
        called when write_eof is called
        """

    def msg_received(self, msg):
        """
        called when msg is called
        """
    def event_received(self, event):
        """
        called when event is called
        """
    def callback_received(self,callback):
        """
        called when callback is called
        """
class QAR_StreamProtocol(QAR_Protocol):
    def __init__(self, stream, loop):
        self._loop = loop
        self._stream = stream
        self._paused = False
        self._drain_waiter = None
        self._connection_lost = False

    def pause_writing(self):
        assert not self._paused
        self._paused = True

    def resume_writing(self):
        assert self._paused
        self._paused = False
        waiter = self._drain_waiter
        if waiter is not None:
            self._drain_waiter = None
            if not waiter.done():
                waiter.set_result(None)

    def connection_made(self, transport):
        self._stream.set_transport(transport)

    def connection_lost(self, exc):
        self._connection_lost = True
        if exc is None:
            self._stream.feed_closing()
        else:
            self._stream.set_exception(exc)
        if not self._paused:
            return
        waiter = self._drain_waiter
        if waiter is None:
            return
        self._drain_waiter = None
        if waiter.done():
            return
        if exc is None:
            waiter.set_result(None)
        else:
            waiter.set_exception(exc)

    @asyncio.coroutine
    def _drain_helper(self):
        if self._connection_lost:
            raise ConnectionResetError('Connection lost')
        if not self._paused:
            return
        waiter = self._drain_waiter
        assert waiter is None or waiter.cancelled()
        waiter = asyncio.Future(loop=self._loop)
        self._drain_waiter = waiter
        yield from waiter

    def msg_received(self, msg):
        self._stream.feed_msg(msg)

    def event_received(self, event):
        self._stream.feed_event(event)
    def data_received(self, data):
        self._stream.feed_msg(data)
    def callback_received(self, callback):
        self._stream.feed_msg(callback)