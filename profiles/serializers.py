from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model.
    """
    class Meta:
        model = Profile
        fields = ('id', 'bio', 'location', 'interests')
