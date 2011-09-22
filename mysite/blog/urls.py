from django.conf.urls.defaults import patterns, include, url
from blog import views

from haystack.views import SearchView, search_view_factory
from haystack.query import SearchQuerySet
from forms import EntrySearchForm

urlpatterns = patterns('',
    
    url(r'^$', views.blog_index),
    
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug>[-\w]+)/$', views.blog_entry_detail),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', views.blog_entries_month),
    url(r'^(?P<year>\d{4})/$', views.blog_entries_year),

    url(r'^tags/(?P<slug>[-\w]+)/$', views.tag_detail),
    url(r'^tags/$', views.tag_list),
    
    url(r'^authors/(?P<author>[-\w]+)/$', views.author_detail),
    url(r'^authors/$', views.author_list),
    
) 

#Haystack search url and view call
urlpatterns += patterns('haystack.views',
    url(r'^search/$', search_view_factory(
        view_class=SearchView,
        template='blog/search.html',
        searchqueryset=SearchQuerySet(),
        form_class=EntrySearchForm,
        results_per_page=10,
    ), name='haystack_search'),
)
