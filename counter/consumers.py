from channels.generic.websocket import AsyncWebsocketConsumer


class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print(self.scope)
        await self.accept()

    async def disconnect(self, code):
        await self.disconnect(code)

    async def receive(self, text_data):
        print(text_data)
        pass
