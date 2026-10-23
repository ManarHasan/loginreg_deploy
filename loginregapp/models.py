from django.db import models

# Create your models here.
class UserManager(models.Manager):
  def validate_user(self, username, password):
    errors = {}
    if len(username) < 2:
      errors['username'] = 'Must be at least 3 characters'

    return errors


class User(models.Model):
  username = models.CharField(max_length=255, unique=True)
  password = models.CharField(max_length=255)
  objects = UserManager()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
