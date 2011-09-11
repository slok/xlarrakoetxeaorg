from django.db.models import Manager
import datetime

class PublishedManager(Manager):
        """Queryset to retrieve published post"""
        
        def get_query_set(self):
            """get published entries and that are in the past (published future ones, aren't published in thory)
            Orders objects by publiched date (descending) and if are conflicts with title (not normal)"""
            return super(PublishedManager, self).get_query_set().filter(status='p', pub_date__lte=datetime.datetime.now()).order_by('-pub_date', 'title')
        
