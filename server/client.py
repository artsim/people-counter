import json
import random
import time
import uuid

import websocket

ws = websocket.WebSocket()

ws.connect("ws://localhost:8000/ws/polldata/")

device_id = uuid.uuid4()

for _ in range(1000):
    ws.send(
        json.dumps({"device_id": str(device_id), "people_count": random.randint(4, 10)})
    )
    time.sleep(10)
