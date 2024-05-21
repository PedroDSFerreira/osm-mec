import websockets
import json
import asyncio
import queue
import threading
import asyncio
from cherrypy.process import plugins
import os

ws = []
metrics_queue = queue.Queue()

class WebSocketServiceThread(plugins.SimplePlugin):
    """Background thread that sends metrics to the websockets"""


    def __init__(self, bus):
        super().__init__(bus)
        self.t = None

    def start(self):
        """Plugin entrypoint"""

        self.t = threading.Thread(target=self.run_server)
        self.t.daemon = True
        self.t.start()

    def run_server(self):
        try:
            asyncio.run(send_metrics())
        except Exception as e:
            print(f"Could not start websockets server: {e}")
            pass

async def send_metrics():
    async with websockets.serve(receive_connection, "0.0.0.0", os.getenv("OSS_WS_PORT")):
        try:
            while True:
                if not metrics_queue.empty():
                    metrics = metrics_queue.get()
                    for websocket in ws:
                        await websocket.send(json.dumps(metrics))
                await asyncio.sleep(0.1)

        except Exception as e:
            print(f"Could not send metrics: {e}")
            pass

async def receive_connection(websocket, path):
    ws.append(websocket)
    try:
        async for message in websocket:
            await websocket.wait_closed()
    finally:
        ws.remove(websocket)
