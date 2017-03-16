#!/usr/bin/env python

import SimpleHTTPServer
import SocketServer
import sys

port = sys.argv[1]

handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("0.0.0.0", int(port)), handler)

httpd.serve_forever()
