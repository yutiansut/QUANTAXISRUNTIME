import argparse
import logging
import os
import sys

import zmq

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pzmq
from gen import message_pb2 as gen
import service


def call_echo(client):
    req = gen.EchoRequest()
    req.echo = "hello"
    rep = client.echo(req)
    print("Echo of %r is %r" % (req.echo, rep.echo))


def call_add(client):
    req = gen.AddRequest()
    req.a = 3
    req.b = 4
    rep = client.add(req)
    print("%s + %s = %s" % (req.a, req.b, rep.result))


def call_search(client):
    req = gen.SearchRequest()
    req.query = 'man'
    rep = client.search(req)
    print("Search results for %r: %s" % (req.query, [u.name for u in rep.users]))


def main():
    logging.basicConfig()

    parser = argparse.ArgumentParser(description="Launch client")
    parser.add_argument('--connect', '-c', type=str, default="tcp://localhost:8787", help="Where to connect? default: tcp://localhost:8787")

    args = parser.parse_args()

    url = args.connect

    client = pzmq.Client(service.DummyService(), url)

    call_echo(client)
    call_add(client)
    call_search(client)

    print("OK")


if __name__ == '__main__':
    main()
