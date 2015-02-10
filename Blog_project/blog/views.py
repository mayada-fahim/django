from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from blog.models import Comment
from blog.models import user_data,Post
import re
import hashlib

# Create your views here.

def index(request):
	comment_name=request.POST['commentname']
	comment_object=Comment(comment_text=comment_name,comment_type="article")
	comment_object.save();



	return HttpResponse(comment_name)
	#return render(request,'comment.html')
def comment_text(request):
	#return HttpResponse("i am here")
	return render(request,'comment.html')

def home(request):
	posts = Post.objects.all()

	return render(request,'home.html',{'articles': posts})
	
def login_test(request):
    try:
        if request.POST.get('username') == None or request.POST.get('password') == None:
            return render(request,'home.html',{'message':"error"})
            
        else:
            
            users_matches = user_data.objects.all().filter(user_name=request.POST.get('username'), user_password=hashlib.md5(request.POST.get('password')).hexdigest())
            
            if len(users_matches) < 1:
                return render(request,'home.html',{'message':"error")

            else:
                request.session['logged']=True
                request.session['username']=request.POST.get('username')
                return render(request,'home.html')

    except:
        return render(request,'home.html',{'message':"error except"})

def sign_in(request):	
                #return render(request,'home.html')
	return render(request,'sign_in.html')
	
	
def articles(request):
	return render(request,'article.html')


def sign_up(request):
	return render(request,'sign_up.html')

def validate(request):
	username=request.POST['username']
	password=request.POST['password']
	re_password=request.POST['re-password']
	mail=request.POST['mail']
	if username=="":
		message="Please Enter your name"
	elif password=="":
		message="Please Enter Your password"
	elif re_password=="":
		message="Please Confirm Your password"
	elif mail=="":
		message="Please Enter Your E-mail"
	else:
		usernames=user_data.objects.all()
		if usernames.filter(user_name=username):
			message="Please Enter another name"
		elif len(password)<6:
			message="Enter at least 6 character"
		elif password!=re_password:
			message="Password doesn't match"
		elif re.match('^[a-zA-Z0-9._-]+\@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$', mail): #regex for valid mail
			if usernames.filter(user_mail=mail):
				message="Please Enter another e-mail"
			else:
				hashed_password = hashlib.md5(password).hexdigest()
				total_data=user_data(user_name=username,user_password=hashed_password,user_mail=mail,user_status=True)
				total_data.save()
				return HttpResponseRedirect("/home/")
		else:
			message="Please Enter a valid E-mail"
			
	return render(request,'sign_up.html',{'message':message})


def post_html(request):
	posts = Post.objects.all()
	#s=str(Post.post_imageq)
	#new_s=(s.split('/'))[3]
	#return HttpResponse(new_s)
	return render(request,'home.html',{'articles': posts})

def specific_post(request,post_id):
	post = get_object_or_404(Post,pk=post_id)
	imageUrl= str(post.post_image)
	imageName = (imageUrl.split('/'))[3]
	context = {'imageName':imageName,'article':post}
	return render(request,'specific_post.html',context)
