from django import forms
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length = 100)
    content = forms.TextField()

    class Meta:
        model = Post
        fields = ['title', 'content', 'thumb_image', 'file_uplaod']


class CommentForm(forms.ModelForm):
    message = forms.TextField()

    class Meta:
        model = Comment
        fields = ['message']        


class TagForm(forms.ModelForm):
    name = forms.CharField(max_length = 50)         

    class Meta:
        model = Tag
        fields = ['name']   

        
             