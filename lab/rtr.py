"""Minimal isolated RTR v1 fixture; not a production validator."""
import ipaddress
import socketserver
import struct

RECORDS = [
    ("198.51.100.0/26", 65001),
    ("192.0.2.128/25", 65002),
    ("2001:db8:11::/48", 65001),
    ("2001:db8:aaaa::/48", 65002),
]

def header(kind, field, length):
    return struct.pack("!BBHI", 1, kind, field, length)

def prefix(cidr, asn):
    net = ipaddress.ip_network(cidr)
    payload = struct.pack("!BBBB", 1, net.prefixlen, net.prefixlen, 0)
    payload += net.network_address.packed + struct.pack("!I", asn)
    return header(4 if net.version == 4 else 6, 0, 8 + len(payload)) + payload

class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            raw = self.rfile.read(8)
            if len(raw) != 8:
                return
            version, kind, session, length = struct.unpack("!BBHI", raw)
            if version != 1 or length not in (8, 12):
                return
            body = self.rfile.read(length - 8)
            if kind == 2 and length == 8:
                response = header(3, 1, 8)
                response += b"".join(prefix(*record) for record in RECORDS)
            elif kind == 1 and length == 12 and session == 1 and body == struct.pack("!I", 1):
                response = header(3, 1, 8)
            elif kind == 1 and length == 12:
                self.wfile.write(header(8, 0, 8))
                continue
            else:
                return
            response += header(7, 1, 24) + struct.pack("!IIII", 1, 60, 10, 600)
            self.wfile.write(response)

class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

with Server(("0.0.0.0", 3323), Handler) as server:
    server.serve_forever()
