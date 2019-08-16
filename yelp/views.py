from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostCreateForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView




def home(request):
    
    context = {
      'posts': Post.objects.all()
    }
    
    return render(request, 'yelp/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'neighbour/home.html'  
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2
    
    
class PostDetailView(DetailView):
    model = Post
    
    
@login_required  
def post_save(request):
    if request.method =='POST':
    # u_form = UserUpdateForm(request.POST, instance=request.user)
        a_form = PostCreateForm(request.POST, request.FILES)
        if a_form.is_valid():
            image = a_form.save(commit=False)
            image.author = request.user
            # u_form.save()
            image.save()
            return redirect('yelp-home')
    else:
        a_form = PostCreateForm()
    return render(request,'yelp/post_form.html',{'form':a_form})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    
class UserPostListView(ListView):
    model = Post
    template_name = 'neighbour/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    


def about(request):
    return render(request, 'yelp/about.html', {'title': 'About'})


