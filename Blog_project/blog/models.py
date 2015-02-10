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
	
	#post = models.ForeignKey(Post) #after creating model post 
class user_data(models.Model):
	user_name=models.CharField(max_length=100,unique=True,primary_key=True)
	user_password=models.CharField(max_length=100)
	user_mail=models.EmailField(max_length=75,unique=True)
	user_status=models.BooleanField(default=False)