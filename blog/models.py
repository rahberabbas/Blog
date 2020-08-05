from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=1000)
    header_image = models.ImageField(null='True', blank= 'True', upload_to= 'images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    currentdate= models.DateField(default=timezone.now)
    ctime = models.TimeField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name="blog_post")

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        # return reverse('detail',args=(str(self.id)))
        return reverse('index')

class Profile(models.Model):
    user = models.OneToOneField(User, null='True', on_delete=models.CASCADE)
    bio = models.TextField(max_length=10000)
    profile_pic = models.ImageField(null='True', blank= 'True', upload_to= 'images/profile')
    instagram_url = models.CharField(max_length=1000, null='True', blank= 'True')
    facebook_url = models.CharField(max_length=1000, null='True', blank= 'True')
    gmail_url = models.CharField(max_length=1000, null='True', blank= 'True')

    def __str__(self):
        return str(self.user)

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
