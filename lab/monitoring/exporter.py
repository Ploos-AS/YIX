"""Lab-only read-only BIRD metrics endpoint."""
import subprocess
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

def metrics():
    output = subprocess.check_output(["birdc", "-r", "show", "protocols"], text=True, timeout=5)
    lines = ["# TYPE muix_bgp_session_up gauge"]
    for line in output.splitlines():
        fields = line.split()
        if len(fields) >= 2 and fields[1] == "BGP":
            name = fields[0]
            if not name.isascii() or not name.replace("_", "").isalnum():
                continue
            lines.append(f'muix_bgp_session_up{{peer="{name}"}} {int("Established" in fields)}')
    for table in ("master4", "master6", "lab_roa4", "lab_roa6"):
        output = subprocess.check_output(["birdc", "-r", "show", "route", "table", table, "count"], text=True, timeout=5)
        import re
        match = re.search(r"(\d+) of (\d+) routes", output)
        if not match:
            raise ValueError("Unexpected route count output")
        lines.append(f'muix_bird_routes{{table="{table}"}} {match.group(1)}')
    return "\n".join(lines) + "\n"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/metrics":
            self.send_error(404)
            return
        try:
            body = metrics().encode()
        except (subprocess.SubprocessError, ValueError):
            self.send_error(503)
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/plain; version=0.0.4")
        self.end_headers()
        self.wfile.write(body)

if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 9105), Handler).serve_forever()
