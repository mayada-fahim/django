from django.db import models

# Create your models here.


class Post(models.Model):
	post_text = models.CharField(max_length=250)
	post_date = models.DateTimeField('date published')
class Comment(models.Model):
	comment_text = models.CharField(max_length=250)
	
	post = models.ForeignKey(Post) #after creating model post 