from __future__ import unicode_literals
from ..login_app.models import User

from django.db import models

# Create your models here.
class Comment(models.Model):
	content = models.CharField(max_length=255)
	poster = models.ForeignKey(User, related_name='posts', default= None)
	user = models.ForeignKey(User, related_name='comments')

