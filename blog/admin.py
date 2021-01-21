from django.contrib import admin
from blog.models import Blog, BlogComment
from blog.models import Contact
from blog.models import Tag
from blog.models import About
from blog.models import Todo
from blog.models import SocialContact
from blog.models import FrontPage
# Register your models here.
# admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(About)
admin.site.register(Todo)
admin.site.register(Tag)
admin.site.register(FrontPage)
admin.site.register(SocialContact)
admin.site.register((BlogComment))

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    class Media:
        js = ('tinyInject.js',)
