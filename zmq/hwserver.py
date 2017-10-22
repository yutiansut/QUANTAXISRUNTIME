#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq
from stock_min_pb2 import stock_min
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    #  Wait for next request from client
    message = socket.recv()
    print("Received request: %s" % message)

    #  Do some 'work'
    #time.sleep(1)
    b=stock_min()
    b.open=1
    b.close=2
    b.high=100
    b.low=1

    #  Send reply back to client
    socket.send(b.SerializeToString())