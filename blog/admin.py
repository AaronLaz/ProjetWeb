from django.contrib import admin

from blog.models import BlogPost, Comment
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(BlogPost, BlogAdmin)
admin.site.register(Comment)