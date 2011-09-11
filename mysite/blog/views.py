from django.shortcuts import render_to_response
from django.template import RequestContext
from mysite.blog.models import Entry

def blog_index(request):
    entries = Entry.published_objects.all()
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
