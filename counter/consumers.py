import json

from channels.generic.websocket import AsyncWebsocketConsumer


class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.groupname = "counter"
        await self.channel_layer.group_add(self.groupname, self.channel_name)
        await self.accept()

    async def disconnect(self, code):
        await self.disconnect(code)

    async def receive(self, text_data):
        data = json.loads(text_data)
        await self.channel_layer.group_send(
            self.groupname, {"type": "processing", "value": data}
        )

    async def processing(self, event):
        data = event["value"]
        await self.send(text_data=json.dumps(data))
