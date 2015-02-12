from __future__ import division
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from blog.models import Comment
from blog.models import user_data,Post
import re
import hashlib
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
import math;



# Create your views here.


def index(request):
	comment_name=request.POST['commentname']
	comment_object=Comment(comment_text=comment_name,comment_type="article")
	comment_object.save();



	return HttpResponse(comment_name)
	#return render(request,'comment.html')
def comment(request,post_id):
	#post = get_object_or_404(Post,pk=post_id)

	comment_name=request.POST['commentname']
	comment_object=Comment(comment_text=comment_name,comment_type="article",post_id_id=post_id)
	comment_object.save();
	post = get_object_or_404(Post,pk=post_id)
	imageUrl= str(post.post_image)
	imageName = (imageUrl.split('/'))[3]
	#return HttpResponse(post_id)
	context = {'imageName':imageName,'article':post,'post_id':post_id }
	return render(request,'article.html',context)
	#return HttpResponse(comment_name)

def home(request):
	imageNames=[]
	pages=[]
	posts = Post.objects.all().order_by('-post_date')[:2]
	posts_images=Post.objects.all().order_by('-post_date')
	records_count = Post.objects.all().count()
	number_of_pages = int(math.ceil(float(records_count/2)));
	for page in range(number_of_pages):
		pages.append(page+int(1))


	for image in posts_images:
		imageUrl= str(image.post_image)
		imageNames.append((imageUrl.split('/'))[3])	
		
	return render(request,'home.html',{'articles': posts , 'images' : imageNames , 'pages_count':pages})
	
#def login_test(request):
	# try:
    #     if request.POST.get('username') == None or request.POST.get('password') == None:
    #         #return render(request,'home.html',{'message':"error"})
    #         #url = reverse('blog.views.home')
    #         #return HttpResponseRedirect(url)
    #         return redirect('/home/?message="errorrrr"',message="errorjrrrrrrrrrrrrrrrrrrrrrr")
            
    #     else:
            
    #         users_matches = user_data.objects.all().filter(user_name=request.POST.get('username'), user_password=hashlib.md5(request.POST.get('password')).hexdigest())
            
    #         if len(users_matches) < 1:
    #             return redirect('/home/?message="errorrrrr"',message="errorjrrrrrrrrrrrrrrrrrrrrrr")

    #         else:
    #             request.session['logged']=True
    #             request.session['username']=request.POST.get('username')
    #             #return render(request,'home.html')
    #             return HttpResponseRedirect("/home/")

    # except:
    #     return redirect('/home/?message="errorr"',message="errorjrrrrrrrrrrrrrrrrrrrrrr")
    
	# try:
	# 	if request.POST.get('username') == None or request.POST.get('password') == None:
	# 		return render(request,'sign_in.html')
	# 	else:
	# 		users_matches = User.objects.all().filter(username=request.POST.get('username'), password=request.POST.get('password'))
	# 		if len(users_matches) < 1:
	# 			return render(request,'sign_in.html')
	# 		else:
	# 			response = render(request,'home.html')
	# 			if "check1" in request.POST.keys():
	# 				request.session['logged']=True
	# 				request.session['username']=request.POST.get('username')
	# 				response.set_cookie(key='user',value=request.POST.get('username'),max_age=60*100)
	# 				return response
                   
	# 			elif "check2" in request.POST.keys():
	# 				request.session['logged']=True
	# 				request.session['username']=request.POST.get('username')
	# 				response.delete_cookie('user')
	# 				return response
	# 			elif request.session['logged']== True :
	# 				request.session['username']=request.POST.get('username')
	# 				return render(request,'home.html')
	# 			else:
	# 				return render(request,'sign_in.html')

	# except:
	# 	return render(request,'sign_in.html')


def sign_in(request):
	
	return render(request,'sign_in.html')
	#return HttpResponse(signFlag)
	
	
def articles(request,post_id,page_id):
	comment_name=request.POST.get('commentnamee')
	
	if comment_name!=None:
		comment_object=Comment(comment_text=comment_name,comment_type="article",post_id_id=post_id)
		comment_object.save();
		post = get_object_or_404(Post,pk=post_id)
		imageUrl= str(post.post_image)
		imageName = (imageUrl.split('/'))[3]
	#return HttpResponse(post_id)
		context = {'imageName':imageName,'article':post,'post_id':post_id }
		return render(request,'article.html',context)
	else:	
		post = get_object_or_404(Post,pk=post_id)
		imageUrl= str(post.post_image)
		imageName = (imageUrl.split('/'))[3]

		context = {'imageName':imageName,'article':post,'post_id':post_id}
		return render(request,'article.html',context)

def page(request,page_id):
	# mafrood awel 7aga a5od el page_id we ageb el data bta3to mn el table we m3ah 2 kman 
	posts_per_page =get_object_or_404(Post,id=int(page_id)+1)
	#posts_per_page2 = get_object_or_404(Post,id=int(page_id)+2)
	
	return render(request,"page.html",{'posts_page':posts_per_page })#, 'posts_page2':posts_per_page2})


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
				if 'image' in request.FILES:
					image=request.FILES["image"]
				else:
					image="null"
				
				hashed_password = hashlib.md5(password).hexdigest()
				total_data=user_data(user_name=username,user_password=hashed_password,user_mail=mail,user_status=True,user_image=image)
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
