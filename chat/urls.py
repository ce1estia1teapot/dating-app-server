from django.urls import path
from .views import ConversationListView

urlpatterns = [
    path('conversations/', ConversationListView.as_view(), name='conversation-list'),
]
