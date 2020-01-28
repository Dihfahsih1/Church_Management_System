from django.shortcuts import render, get_object_or_404
#from django.contrib import messages
from .models import posts
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
def home(request):
    Posts=posts.objects.all()
    context={
    'Posts': Posts
    }
    return render(request,'blog/home.html', context)
class PostListView(ListView):
    model = posts
    template_name = 'blog/home.html' #<app_name>/<model>_<viewtype>.html
    context_object_name = 'Posts'
    ordering = ['-Date_posted']
    paginate_by = 4

class UserPostListView(ListView):
    model = posts
    template_name = 'blog/user_posts.html' #<app_name>/<model>_<viewtype>.html
    context_object_name = 'Posts'
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return posts.objects.filter(Name=user).order_by('-Date_posted')
class PostDetailView(DetailView):
    model = posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = posts
    fields = ['Title','Post_content']
    def form_valid(self, form):
        form.instance.Name = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = posts
    fields = ['Title','Post_content']
    def form_valid(self, form):
        form.instance.Name = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Name:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = posts
    #messages.success('Post Deleted Successfully!')
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.Name:
            return True
        return False
def about(request):
    return render(request,'blog/about.html',{'Title':'About'})
