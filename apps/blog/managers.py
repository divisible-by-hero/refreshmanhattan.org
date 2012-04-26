from django.db.models import Manager

class PostManager(Manager):
    def published(self):
        return self.model.objects.filter(published=True)