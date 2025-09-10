from rest_framework import serializers
from .models import Swipe, Match

class SwipeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Swipe model. Used to create a new swipe.
    """
    class Meta:
        model = Swipe
        fields = ('id', 'swiped_on', 'is_match')
        read_only_fields = ('is_match',)

class MatchSerializer(serializers.ModelSerializer):
    """
    Serializer for the Match model.
    """
    # The users' full data can be included in the response.
    user1 = serializers.CharField(source='user1.username', read_only=True)
    user2 = serializers.CharField(source='user2.username', read_only=True)

    class Meta:
        model = Match
        fields = ('id', 'user1', 'user2', 'timestamp')
