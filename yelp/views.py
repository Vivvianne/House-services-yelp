from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
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
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            
            post.save()
            return redirect('neighbour-home')
    else:
        form = PostCreateForm()
        
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.neighbourhood_id = self.request.neighbourhood
        return super().form_valid(form)
    return render(request,'neighbour/post_form.html',{'form':form})


def about(request):
    return render(request, 'yelp/about.html', {'title': 'About'})


