from django.db.models import Manager
from django.db.models.query import QuerySet

class PostQuerySet(QuerySet):
    def published(self):
        return self.filter(published=True)

class PostManager(Manager):
    def get_query_set(self):
        return PostQuerySet(self.model, using=self._db)

    def published(self):
        return self.get_query_set().published()