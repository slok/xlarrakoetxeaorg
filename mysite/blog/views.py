from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from mysite.blog.models import Entry

#Objects for the pagination
OBJECTS_PER_PAGE = 2

def blog_index(request):
    
    entries = _get_paginated_objects(Entry.published_objects.all(), request, 1)
    
    data = { 
        'entries' : entries,
    }
    
    return render_to_response('blog/blog_index.html', data, context_instance=RequestContext(request))

def blog_entry_detail(request, year, month, day, slug):
    data = { 
        '' : '',
    }
    
    return render_to_response('blog/blog_index.html', data, context_instance=RequestContext(request))

def blog_entries_month(request, year, month):
    data = { 
        '' : '',
    }
    
    return render_to_response('blog/blog_index.html', data, context_instance=RequestContext(request))

def blog_entries_year(request, year):
    data = { 
        '' : '',
    }
    
    return render_to_response('blog/blog_index.html', data, context_instance=RequestContext(request))

#####################################################################################################

def _get_paginated_objects(objects, request, opp=OBJECTS_PER_PAGE):
    
    paginator = Paginator(objects, opp)
    
    try:
        page = int(request.GET.get('page'))
    except (ValueError, TypeError):
        page = 1
   
    try:
        objects = paginator.page(page)
    except  InvalidPage, EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        objects = paginator.page(paginator.num_pages)
    
    return objects
