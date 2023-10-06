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
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.call_alert_task = None  # Initialize the task variable

    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

        # Start the periodic task to send updates
        self.call_alert_task = asyncio.create_task(self.newCallAlert())

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

        # Cancel the task when disconnecting
        if self.call_alert_task:
            self.call_alert_task.cancel()

    async def newCallAlert(self):
        initTime = time.time()
        sentObjects = []
        objs = await Calls_objects_all()  # Await the asynchronous query
        for o in objs:
            if o.creation_date > initTime:
                sentObjects.append(o.id)

                text_data = dict(o)
                print(text_data)

                await self.send(text_data=json.dumps(text_data))
                await asyncio.sleep(0.10)

        while True:
            try:
                obj = await Calls_objects_latest()  # Await the asynchronous query

                if obj.id not in sentObjects:
                    sentObjects.append(obj.id)

                    text_data = dict(obj)  # Use the 'obj' variable
                    print(text_data)

                    await self.send(text_data=json.dumps(text_data))
                    await asyncio.sleep(0.10)

            except asyncio.CancelledError:
                # Task was cancelled, exit the loop
                break
            except Exception as e:
                print(f'Error occurred: {e}')

                await asyncio.sleep(3)
