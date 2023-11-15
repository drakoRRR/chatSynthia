from django.db import models

from users.models import User


# Create your models here.
class ChatGptBot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    messageInput = models.TextField()
    bot_response = models.TextField()

    def __str__(self):
        return self.user.username


class ChatGptBotImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    messageInput = models.TextField()
    bot_image = models.ImageField(upload_to='users_image_ai')

    def __str__(self):
        return self.user.username

