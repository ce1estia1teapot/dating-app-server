from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Conversation
from .serializers import ConversationSerializer

class ConversationListView(generics.ListAPIView):
    """
    API view to list all conversations for the authenticated user.
    """
    serializer_class = ConversationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Find all conversations where the user is either user1 or user2
        return Conversation.objects.filter(user1=user) | Conversation.objects.filter(user2=user)
