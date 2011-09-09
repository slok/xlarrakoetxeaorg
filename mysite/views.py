from django.shortcuts import render_to_response
from django.conf import settings
from django.template import RequestContext

def index(request):
    
    data = { 
        '' : '',
    }
    
    return render_to_response('index.html', data, context_instance=RequestContext(request))

