from django.core.paginator import Paginator, InvalidPage, EmptyPage

OBJECTS_PER_PAGE = 2

def get_paginated_objects(objects, request, opp=OBJECTS_PER_PAGE):
    
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
