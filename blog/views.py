from django.shortcuts import render , redirect , get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import Post
#This one is imported so no one can create post without being logged in
#we can use signals but in case of classes we have to use mixins
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
#UserPassesTestMixin is required inorder to verify that the author is going to edit and no other person


def home(request):
    post = Post.objects.all()
    return render(request,'blog/home.html',{'posts':post})

def about(request):
    return render(request,'blog/about.html')

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  #<app>/<model>_<name>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4 #it means number of posts per page in home page


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  #<app>/<model>_<name>.html
    context_object_name = 'posts'
    paginate_by = 4 #it means number of posts per page in home page

    def get_queryset(self):
        user = get_object_or_404(User , username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
    model = Post
 
class PostCreateView(LoginRequiredMixin , CreateView):
    model = Post
    fields = ['title','content']

    #for setting the current user to be the author of the post
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin ,UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    #for setting the current user to be the author of the post
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #to check the author is the one who has written the post or someone else
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False


class PostDeleteView(LoginRequiredMixin ,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False