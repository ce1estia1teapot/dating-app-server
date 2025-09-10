from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Swipe, Match
from .serializers import SwipeSerializer, MatchSerializer

class SwipeAPIView(generics.CreateAPIView):
    """
    API view for creating a swipe.
    """
    serializer_class = SwipeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        swiper = self.request.user
        swiped_on = serializer.validated_data['swiped_on']
        
        # Check if a reciprocal swipe exists.
        reciprocal_swipe = Swipe.objects.filter(swiper=swiped_on, swiped_on=swiper, is_match=True).first()

        if reciprocal_swipe:
            # If a reciprocal swipe exists, a match is created.
            Match.objects.create(user1=swiper, user2=swiped_on)
            serializer.save(swiper=swiper, is_match=True)
        else:
            # No reciprocal swipe, so it's not a match yet.
            serializer.save(swiper=swiper, is_match=False)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MatchListView(generics.ListAPIView):
    """
    API view to list all matches for the current user.
    """
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # A user's matches are defined as a Match object where they are either user1 or user2.
        return Match.objects.filter(user1=user) | Match.objects.filter(user2=user)
