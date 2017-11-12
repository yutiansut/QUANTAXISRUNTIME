poc-pzmq
========

RPC with ZMQ + protobuf
Multiple clients may connect to a single endpoint to access a service, the request is then
dispatched to a pool of workers. More details on http://zguide.zeromq.org/page:all#Shared-Queue-DEALER-and-ROUTER-sockets.
