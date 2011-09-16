import datetime
from haystack.indexes import *
from haystack import site
from mysite.blog.models import Entry


class EntryIndex(SearchIndex):
    text = CharField(document=True, use_template=True)
    author = CharField(model_attr='author')
    pub_date = DateTimeField(model_attr='pub_date')

    def index_queryset(self):
        """Used when the entire index for model is updated."""
        return Entry.published_objects.all()


site.register(Entry, EntryIndex)
