from django.urls import reverse
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Post


class PostListing(ListView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = '/'


class PostDetail(DetailView):
    model = Post


class PostUpdate(UpdateView):
    model = Post

    fields = ['title', 'content']

    def get_success_url(self):
        return reverse('blog:detail', kwargs={
            'pk': self.object.pk,
        })


class PostDelete(DeleteView):
    model = Post
    success_url = '/'
