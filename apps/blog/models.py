from django.db import models
from taggit.managers import TaggableManager
from hadrian.utils.slugs import unique_slugify
from django.contrib.auth.models import User
from blog.managers import PostManager

class Category(models.Model):
    name = models.CharField(max_length=160, null=True)
    slug = models.SlugField(editable=False)
    
    def __unicode__(self):
        return self.name

    def save(self):
        unique_slugify(self, self.name)
        super(Category, self).save()

class Post(models.Model):
    title = models.CharField(max_length=250, null=True)
    slug = models.SlugField(editable=False, null=True)
    meta_description = models.CharField(max_length=160, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, blank=True, null=True)
    tags = TaggableManager(blank=True)
    
    extra_head = models.TextField(blank=True, null=True, default='')
    extra_foot = models.TextField(blank=True, null=True, default='')
    
    published = models.BooleanField(default=False)
    date_published = models.DateField(auto_now=True)
    author = models.ForeignKey(User, null=True, editable=False)
    
    objects = PostManager()
    
    def __unicode__(self):
        return self.title
    
    def save(self):
        unique_slugify(self, self.title)
        super(Post, self).save()