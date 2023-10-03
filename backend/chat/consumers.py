# chat/consumers.py
import json
import time

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer

from .models import Message


class TextRoomConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = "chat_%s" % self.room_name

        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)

        self.accept()

        messages = Message.objects.all()

        for message in messages:
            self.receive(message.to_json_dict(), inbuilt=True)

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    def receive(self, text_data, inbuilt=False):
        text_data_json = json.loads(text_data)
        text = text_data_json["text"]
        sender = text_data_json["sender"]

        message = Message(content=text, sender=sender)
        message.save()

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": text, "sender": sender}
        )

        if sender != "Aviquo Official" and not inbuilt:
            time.sleep(1.2)
            self.return_user_message()

    def chat_message(self, event):
        text = event["message"]
        sender = event["sender"]

        self.send(text_data=json.dumps({"text": text, "sender": sender}))

    # simulate instant response (we can create an AI webhook or allow for human response)
    def return_user_message(self):
        message_dict = {"text": "We have received your query, and will get back to you.", "sender": "Aviquo Official"}

        self.receive(json.dumps(message_dict))

        return None
