# -*- coding: utf-8 -*-
from django import template
from tagging.models import Tag
from mysite.blog.models import Entry

register = template.Library()

@register.inclusion_tag('blog/includes/entry_tag_list.html')
def entry_tags(entry):
    return {
        'tags': Tag.objects.get_for_object(entry),
    }

@register.inclusion_tag('blog/includes/side_tag_list.html')
def side_tag_list():
    return {
        'tags': Tag.objects.usage_for_model(Entry, counts=True),
    }
