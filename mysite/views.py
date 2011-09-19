from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext

from mysite.blog.models import Entry

def index(request):
    
    entries = Entry.published_objects.all()[:1]
    
    data = { 
        'entries' : entries,
    }
    
    return render_to_response('index.html', data, context_instance=RequestContext(request))

