from django.contrib import admin
from .models import Post
from .models import Profile, Comment

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comment)

