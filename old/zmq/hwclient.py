import zmq
from stock_min_pb2 import stock_min
context = zmq.Context()

#  Socket to talk to server
print("Connecting to hello world server…")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

#  Do 10 requests, waiting each time for a response
for request in range(10):
    print("Sending request %s …" % request)
    socket.send(b"Hello")
    message=stock_min()
    #  Get the reply.
    #print(socket.recv())
    messager = message.FromString(socket.recv())
    print("Received reply %s [ %s ]" % (messager))