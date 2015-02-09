from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from blog.models import Comment
from blog.models import User,Post

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
            
            users_matches = User.objects.all().filter(username=request.POST.get('username'), password=request.POST.get('password'))
            
            if len(users_matches) < 1:
                return render(request,'home.html',{'message':"error"})

            else:
                request.session['logged']=True
                request.session['username']=request.POST.get('username')
                return render(request,'home.html')

    except:
        return render(request,'home.html',{'message':"error"})

def sign_in(request):
	
                #return render(request,'home.html')
	return render(request,'sign_in.html')
	
	
def articles(request):
	return render(request,'article.html')
def sign_up(request):
	return render(request,'sign_up.html')




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
