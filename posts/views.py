from django.views.generic import ListView
from .models import post

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post

