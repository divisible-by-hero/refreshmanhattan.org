import factory
from blog.models import Post, Category

class PostFactory(factory.Factory):
    FACTORY_FOR = Post
    
    title = "Test Post"
    content = "Helllllllo World"
    published = True
    
class CategoryFactory(factory.Factory):
    FACTORY_FOR = Category
    
    
