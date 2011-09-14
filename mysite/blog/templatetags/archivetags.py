# -*- coding: utf-8 -*-
from django import template
from mysite.blog.models import Entry


register = template.Library()

@register.inclusion_tag('blog/includes/archive_dates_list.html')
def archive_dates():
    return {
        'archive_dates': Entry.published_objects.dates('pub_date', 'month', 'DESC')
    }
 
