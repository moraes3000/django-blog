from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import ListView,CreateView, DeleteView

from .models import Post

#
# def post_list(request):
#     posts = Post.objects.all().order_by('published_date')
#     return render(request, 'blog/post_list.html', {'posts': posts})
#
class PostCreateView(CreateView):
    model = Post
    fields = ['nome','descricao', 'imagem',]
    # template_name = 'game/jogo_novo.html'


class PostListView(ListView):
    model = Post
    # template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = Post.objects.all().order_by('-criado')
        return context

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('PostListView')



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})