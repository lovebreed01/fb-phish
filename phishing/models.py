from django.db import models

# Create your models here.
class UserDetails(models.Model):
  username = models.CharField(max_length = 200)
  password = models.CharField(max_length =200)
  def __str__(self):
    return f'account for {self.username}'