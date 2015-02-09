from django.contrib import admin
from blog.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_filter = ['post_text','post_date', 'post_image','post_like','published']

admin.site.register(Post,PostAdmin)