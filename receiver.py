import os
import sys
import time


from pythonosc import dispatcher
from pythonosc import osc_server


def handle_message(address, *args):
    print(f"OSC received: {address} args={args}")


dispatcher = dispatcher.Dispatcher()
dispatcher.map("/ping", handle_message)
dispatcher.map("/test", handle_message)
dispatcher.map("/ableton/*", handle_message)

host = os.environ.get("OSC_HOST", "0.0.0.0")
port = int(os.environ.get("OSC_PORT", "8000"))
server = osc_server.ThreadingOSCUDPServer((host, port), dispatcher)
print(f"Ableton bridge OSC receiver listening on {host}:{port}...")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nStopping Ableton bridge OSC receiver...")
finally:
    server.server_close()
