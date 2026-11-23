from pythonosc import dispatcher
from pythonosc import osc_server

def handle_message(address, *args):
    print(f"OSC received: {address} args={args}")

dispatcher = dispatcher.Dispatcher()
dispatcher.map("/ping", handle_message)
dispatcher.map("/test", handle_message)
dispatcher.map("/ableton/*", handle_message)

server = osc_server.ThreadingOSCUDPServer(("0.0.0.0", 8000), dispatcher)
print("Ableton bridge OSC receiver listening on UDP port 8000...")
server.serve_forever()
