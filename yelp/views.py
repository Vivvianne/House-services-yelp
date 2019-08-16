from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostCreateForm
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
    paginate_by = 4
    
class PostDetailView(DetailView):
    model = Post
    
    
    
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


def about(request):
    return render(request, 'yelp/about.html', {'title': 'About'})


