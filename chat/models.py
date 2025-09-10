from django.db import models
from users.models import User

class Conversation(models.Model):
    """
    Represents a conversation between two users.
    """
    user1 = models.ForeignKey(User, related_name='conversations1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='conversations2', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation between {self.user1.username} and {self.user2.username}"

class Message(models.Model):
    """
    Represents a single message within a conversation.
    """
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender.username} in conversation {self.conversation.id}"
