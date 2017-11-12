#utf-8


from .low_level_protocol import QAR_Protocol


class QAR_Motor_Protocol(QAR_Protocol):
    
    def connection_made(self,transport):
        self.transport=transport

    def data_received(self,data):
        print(data)


class AsyncMongo_Protocol(QAR_Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()

        print('Data received: {!r}'.format(message))

        print('Send: {!r}'.format(message))
        self.transport.write(data)

        print('Close the client socket')
        self.transport.close()