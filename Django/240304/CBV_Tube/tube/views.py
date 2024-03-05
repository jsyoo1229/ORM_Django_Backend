from django.contrib.auth.mixins  import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy

class PostListView(ListView):
    model = Post

post_list = PostListView.as_view()     



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

    def form_valid(self, form):
        print(f'form: {form}')

        video = form.save(commit = False)
        print(f'video: {video}')

        video.author = self.request.user
        print(f'video.author: {video.author}')
        print(f'super: {super}')

        return super().form_valid(form)
    

post_new = PostCreateView.as_view()    


class PostDetailView(DeleteView):
    model = Post

post_detail = PostDetailView.as_view()


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('tube:post_list')
    template_name = 'tube/form.html'

    def test_func(self):
        return self.get_object().author == self.request.user

post_edit = PostUpdateView.as_view()    


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('tube:post_list')  

    def test_func(self):
        return self.get_object().author == self.request.user  

post_delete = PostDeleteView.as_view()    

