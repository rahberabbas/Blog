from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body', 'header_image' ,'currentdate', 'ctime')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}),
            'author': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Author'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Text'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Text'}),
        }