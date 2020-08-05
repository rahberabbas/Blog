from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Profile, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
# Create your views here.
# def index(request):
#     return render(request,'index.html')

class HomeView(ListView):
    model = Post
    template_name = 'index.html'

class ArticalDetailView(DetailView):
    model = Post
    template_name = 'detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticalDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context

class CreatePost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'

class UpdatePost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    # fields = ['title', 'body']

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')

class ProfilePage(DetailView):
    model = Profile
    template_name = 'profile.html'
    # fields = '__all__'

class About(ListView):
    model = Post
    template_name = 'about.html'

class Contact(ListView):
    model = Post
    template_name = 'contact.html'

class Use(ListView):
    model =Post
    template_name = 'use.html'

def LikeView(request, pk):
    post = get_object_or_404(Post,id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "add_comment.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.post_id =self.kwargs['pk']
        return super().form_valid(form) 