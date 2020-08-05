from django.urls import path,include
# from . import views
from .views import HomeView, ArticalDetailView, CreatePost, UpdatePost, DeletePost, ProfilePage, About, Contact, Use, LikeView, AddCommentView
# from .models import Profile
from . import views
urlpatterns = [
    path('',HomeView.as_view(),name='index'),
    path('articel/<int:pk>',ArticalDetailView.as_view(),name='detail'),
    path('addpost/',CreatePost.as_view(),name= 'add_post'),
    path('articel/edit/<int:pk>',UpdatePost.as_view(),name= 'update_post'),
    path('articel/<int:pk>/remove',DeletePost.as_view(),name= 'delete_post'),
    path('about/',About.as_view(), name = 'about'),
    path('contact/',Contact.as_view(), name = 'contact'),
    path('use/',Use.as_view(), name = 'use'),
    path('like/<int:pk>',LikeView, name = 'like_post'),
    path('articel/<int:pk>/comment/',AddCommentView.as_view(), name= 'comment' )
]
