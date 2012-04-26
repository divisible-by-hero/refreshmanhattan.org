from django.test import LiveServerTestCase
from django.contrib.auth.models import User
from blog.tests.factories import PostFactory, CategoryFactory
from selenium.webdriver.firefox.webdriver import WebDriver
from django.conf import settings

class BlogServerTests(LiveServerTestCase):

    def setUp(self):
        settings.DEBUG = True
        self.category = CategoryFactory.create()
        self.author = User.objects.create_user(username="bob", email="bob@email.com", password="pass")
        self.post = PostFactory.create(category=self.category, author=self.author)
        
        
    @classmethod
    def setUpClass(cls):
        cls.selenium = WebDriver()
        super(BlogServerTests, cls).setUpClass()
        
    @classmethod
    def tearDownClass(cls):
        super(BlogServerTests, cls).tearDownClass()
        #cls.selenium.quit()
        
    def test_view_post(self):
        print(self.post.get_absolute_url())
        self.selenium.get("%s%s" % (self.live_server_url, self.post.get_absolute_url()))
        