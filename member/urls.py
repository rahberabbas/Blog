from django.urls import path,include
from .views import UserRegisterView, UserEditView, ProfilePage

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    # path('<int:pk>/profile/',ProfilePage.as_view(), name='profile_page')
]
