from django.shortcuts import render
from blog.models import *
from django.views.generic import DetailView

class PostDetailView(DetailView):
    
    context_object_name = "post"
    template_name = "blog/post_detail.html"
    queryset = Post.objects.published()
    
        