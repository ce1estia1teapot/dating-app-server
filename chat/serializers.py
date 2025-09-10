from rest_framework import serializers
from .models import Conversation, Message

class MessageSerializer(serializers.ModelSerializer):
    """
    Serializer for the Message model.
    """
    sender_username = serializers.CharField(source='sender.username', read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'sender', 'text', 'timestamp', 'sender_username')

class ConversationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Conversation model, including the last message.
    """
    other_user = serializers.SerializerMethodField()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ('id', 'other_user', 'last_message')

    def get_other_user(self, obj):
        # Determine the other user in the conversation
        if self.context['request'].user == obj.user1:
            return obj.user2.username
        return obj.user1.username

    def get_last_message(self, obj):
        # Get the last message in the conversation
        last_message = obj.messages.order_by('-timestamp').first()
        if last_message:
            return MessageSerializer(last_message).data
        return None
