from django.urls import path
from .views import ProfileAPIView, ProfileListView

urlpatterns = [
    # API endpoint to retrieve or update the authenticated user's own profile.
    path('me/', ProfileAPIView.as_view(), name='my-profile'),
    
    # API endpoint to list all profiles that could be potential matches for the user.
    path('matches/', ProfileListView.as_view(), name='potential-matches'),
]
