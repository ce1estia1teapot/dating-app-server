from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer

class ProfileAPIView(generics.RetrieveUpdateAPIView):
    """
    API view for retrieving and updating a user's own profile.
    
    This view ensures that a user can only interact with their own profile,
    providing a secure way to manage personal information.
    """
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # The user can only access their own profile.
        # This is a key security measure.
        return self.request.user.profile

class ProfileListView(generics.ListAPIView):
    """
    API view to list potential matches (all other profiles).
    
    This view returns a list of profiles that the current user has not yet
    interacted with, effectively serving as the "swipe" deck.
    """
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Exclude the current user's profile from the list of potential matches.
        # This prevents users from being matched with themselves.
        return Profile.objects.exclude(user=self.request.user)
