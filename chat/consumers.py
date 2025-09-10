import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message, Conversation
from users.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    """
    WebSocket consumer for real-time chat.
    """
    async def connect(self):
        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.conversation_group_name = f'chat_{self.conversation_id}'

        # Join the conversation group
        await self.channel_layer.group_add(
            self.conversation_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the conversation group
        await self.channel_layer.group_discard(
            self.conversation_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Receive message from WebSocket.
        """
        data = json.loads(text_data)
        message_text = data['message']
        sender_id = data['sender_id']

        # Save the message to the database
        message = await self.save_message(sender_id, message_text)

        # Send the message to the group
        await self.channel_layer.group_send(
            self.conversation_group_name,
            {
                'type': 'chat_message',
                'message': message_text,
                'sender': sender_id,
            }
        )

    async def chat_message(self, event):
        """
        Receive message from the group and send it to the WebSocket.
        """
        message = event['message']
        sender = event['sender']

        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
        }))

    @sync_to_async
    def save_message(self, sender_id, text):
        """
        Helper function to save the message to the database.
        """
        conversation = Conversation.objects.get(id=self.conversation_id)
        sender = User.objects.get(id=sender_id)
        return Message.objects.create(conversation=conversation, sender=sender, text=text)
