from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    # portfolio = models.ManyToOneRel(User, on_delete=)

    def __str__(self):
        return f"{self.user.username} Profile"