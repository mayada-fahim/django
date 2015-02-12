from django.contrib import admin
from blog.models import Post,user_data
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display=['post_text','post_date','post_image','post_like','published']
	list_filter = ['post_date','published']
class user_dataAdmin(admin.ModelAdmin):
	list_display=['user_name','user_password','user_mail','user_status']
	list_filter = ['user_name']
admin.site.register(Post,PostAdmin)
admin.site.register(user_data,user_dataAdmin)