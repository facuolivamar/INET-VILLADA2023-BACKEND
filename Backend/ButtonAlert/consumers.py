# consumers.py
import json
import asyncio
import re
import time
from BackendApp.models import Calls

import os

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer


@database_sync_to_async
def Calls_objects_all():
    return Calls.objects.all()

@database_sync_to_async
def Calls_objects_latest():
    return Calls.objects.latest('creationDateTime')

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

        # Start the periodic task to send updates
        asyncio.create_task(self.newCallAlert())

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def newCallAlert(self):
        initTime = time.time()
        sentObjects = []
        objs = Calls_objects_all()
        for o in objs:
            if o.creation_date > initTime:
                sentObjects.append(o.id)

                text_data = dict(o)
                print(text_data)

                await self.send(text_data=json.dumps(text_data))
                await asyncio.sleep(0.10)

        while True:
            try:
                obj = Calls_objects_latest()

                if obj.id not in sentObjects:
                    sentObjects.append(obj.id)

                    text_data = dict(o)
                    print(text_data)

                    await self.send(text_data=json.dumps(text_data))
                    await asyncio.sleep(0.10)

            except Exception as e:
                print(f'Error occurred: {e}')

                await asyncio.sleep(3)