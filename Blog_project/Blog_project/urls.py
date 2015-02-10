from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'Blog_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$','blog.views.index'),
    url(r'^comment/$','blog.views.comment_text'),
	url(r'^home/$','blog.views.home'),
    url(r'^home/login_test/$','blog.views.login_test'),
	url(r'^sign_in/$','blog.views.sign_in'),
	url(r'^article/$','blog.views.articles'),
	url(r'^sign_up/$','blog.views.sign_up'),
    url(r'^validate/$','blog.views.validate'),

    #url(r'^index/(?P<post_id>\d+)/$','blog.views.index'),
    # another url here index/post_id to determine which post
]
