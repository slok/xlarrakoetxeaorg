# -*- coding: utf-8 -*-
from django import template
from tagging.models import Tag


register = template.Library()

@register.inclusion_tag('blog/includes/entry_tag_list.html')
def entry_tags(entry):
    return {
        'tags': Tag.objects.get_for_object(entry),
    }
