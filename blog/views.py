from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin)
from django.contrib.auth.models import User
from django.shortcuts import (
    get_object_or_404,
    render)
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()}
    return render(
        request,
        'blog/home.html',
        context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title',
        'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = [
        'title',
        'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return True if self.request.user == post.author else False


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(
            User,
            username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


def about(request):
    return render(
        request,
        'blog/about.html',
        {'title': 'About'})
