from django.db import models

# Create your models here.


class Post(models.Model):
	post_text = models.CharField(max_length=250)
	post_date = models.DateTimeField('date published')
	post_image=models.ImageField(upload_to = "static/images/article",default='null')
	post_like=models.IntegerField(default=0)
	published=models.BooleanField(default=False)

class Comment(models.Model):
	comment_text = models.CharField(max_length=250)
	comment_type=models.CharField(max_length=10)
	
	post_id = models.ForeignKey(Post,default=1) #after creating model post 
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)