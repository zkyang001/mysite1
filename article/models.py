from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=30)
	content = models.TextField()
	create_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now=True)
	author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
	is_deleted = models.BooleanField(default=False)
	readed_num = models.IntegerField(default=0)