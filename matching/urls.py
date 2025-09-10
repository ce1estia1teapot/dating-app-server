from django.urls import path
from .views import SwipeAPIView, MatchListView

urlpatterns = [
    # Endpoint for a user to swipe on another user.
    path('swipe/', SwipeAPIView.as_view(), name='swipe'),
    
    # Endpoint to retrieve a list of all mutual matches.
    path('matches/', MatchListView.as_view(), name='matches'),
]
