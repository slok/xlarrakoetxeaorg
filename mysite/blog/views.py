from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import Http404
from django.utils.translation import ugettext as _
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned 
from django.contrib.auth.models import User

import datetime

from mysite.blog import utils
from mysite.blog.models import Entry

from tagging.models import Tag, TaggedItem
from tagging.utils import get_tag, get_queryset_and_model


def blog_index(request):
    
    entries = utils.get_paginated_objects(Entry.published_objects.all(), request)
    
    data = { 
        'entries' : entries,
    }
    
    return render_to_response('blog/blog_index.html', data, context_instance=RequestContext(request))

def blog_entry_detail(request, year, month, slug):
    
    #There are no entries or are more than one: 404 page not found
    
    try:
        entry = Entry.published_objects.get(slug=slug, pub_date__year = int(year), pub_date__month = int(month))
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        raise Http404
    
    data = { 
        'entry' : entry,
    }
   
    return render_to_response('blog/blog_entries_detail.html', data, context_instance=RequestContext(request))

def blog_entries_month(request, year, month):
    
    entries = Entry.published_objects.all().filter(pub_date__year = int(year), pub_date__month = int(month))
    entries = utils.get_paginated_objects(entries, request)
    date = datetime.datetime(int(year), int(month), 1)
    
    data = { 
        'entries' : entries,
        'entries_date': date,
    }
    
    return render_to_response('blog/blog_entries_month.html', data, context_instance=RequestContext(request))

def blog_entries_year(request, year):
    
    entries = Entry.published_objects.all().filter(pub_date__year = int(year))
    entries = utils.get_paginated_objects(entries, request)
    
    date = datetime.datetime(int(year), 1, 1)
    
    data = { 
        'entries' : entries,
        'entries_date' : date,
    }
    
    return render_to_response('blog/blog_entries_year.html', data, context_instance=RequestContext(request))

def tag_detail(request, slug):
    
    #piece of code obtained from tagging.views
    
    queryset_or_model = Entry.published_objects.all()
    
    tag_instance = get_tag(slug)
    
    if tag_instance is None:
        raise Http404(_('No Tag found matching "%s".') % slug)
    
    queryset = TaggedItem.objects.get_by_model(queryset_or_model, tag_instance)
    
    #now paginate the resultants (maybe there are many posts with this tag)
    entries = utils.get_paginated_objects(queryset, request, 10)
    
    data = { 
        'entries' : entries,
        'tag': tag_instance,
    }
    
    return render_to_response('blog/blog_index.html', data, context_instance=RequestContext(request))
    
def tag_list(request):

    tag_cloud = Tag.objects.cloud_for_model(Entry, steps=3, filters=dict(status='p'))
    data = { 
        'tag_cloud' : tag_cloud,
    }
    
    return render_to_response('blog/tag_list.html', data, context_instance=RequestContext(request))

def author_detail(request, author):
    
    try:
        author = User.objects.get(username = author)
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        raise Http404
        
    queryset = Entry.published_objects.all().filter(author=author)
    entries = utils.get_paginated_objects(queryset, request, 10)
    data = { 
        'author' : author,
        'entries': entries,
    }
    
    return render_to_response('blog/blog_index.html', data, context_instance=RequestContext(request))


def author_list(request):
    
    authors = User.objects.all()
    author_list = []
    
    # Create list with authors tuple: (username, number of entries)
    for author in authors:
        aux_author = (author.username, Entry.published_objects.all().filter(author=author).count() ) 
        author_list.append(aux_author)
    
    data = { 
        'authors' : author_list,
    }
    
    return render_to_response('blog/author_list.html', data, context_instance=RequestContext(request))

