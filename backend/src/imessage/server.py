import socketio
sio = socketio.AsyncServer()
app = socketio.ASGIApp(sio)
class Server:
    def __init__(self, port):
        self.port = port

    @sio.event
    async def connect(self, sid, environ):
        print(f"connect {sid}")
        await sio.emit("message", "hello", room=sid)



