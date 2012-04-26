from django.conf.urls import patterns, include, url
from blog.views import PostDetailView
from blog.models import Post


urlpatterns = patterns('',  
    url(r'^post/(?P<slug>[-\w]+)/$', PostDetailView.as_view()),
)