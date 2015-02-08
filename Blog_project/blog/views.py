from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Comment

# Create your views here.

def index(request):
	


	
	return render(request,'comment.html')
