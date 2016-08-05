from django.contrib import admin
from blog.models import Post, Comment, Tag, Zipcode
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Zipcode)

