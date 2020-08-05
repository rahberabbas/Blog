from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic import DetailView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignupForm
from blog.models import Profile
# Create your views here.

class ProfilePage(DetailView):
    model = Profile
    template_name = 'registration/profile.html'

    

    def get_context_data(self, **kwargs):
        users = Profile.objects.all()
        context = super(ProfilePage, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        return super().get_context_data(**kwargs)
        context['page_user']= page_user
        return context

class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user