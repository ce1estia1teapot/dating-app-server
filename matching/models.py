from django.db import models
from users.models import User

class Swipe(models.Model):
    """
    Records a user's swipe action on another user.
    """
    swiper = models.ForeignKey(User, related_name='swipes_made', on_delete=models.CASCADE)
    swiped_on = models.ForeignKey(User, related_name='swipes_received', on_delete=models.CASCADE)
    is_match = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures a user can only swipe on another user once.
        unique_together = ('swiper', 'swiped_on')
        # Explicitly name the table in case of database collision.
        db_table = 'app_swipe'

    def __str__(self):
        return f"{self.swiper.username} swiped on {self.swiped_on.username}"

class Match(models.Model):
    """
    Represents a successful match between two users.
    """
    user1 = models.ForeignKey(User, related_name='matches1', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, related_name='matches2', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Ensures a match between two users is only created once.
        unique_together = ('user1', 'user2')
        # Explicitly name the table.
        db_table = 'app_match'

    def __str__(self):
        return f"{self.user1.username} and {self.user2.username} are a match"
