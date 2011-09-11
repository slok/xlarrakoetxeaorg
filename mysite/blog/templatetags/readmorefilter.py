# -*- coding: utf-8 -*-
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@stringfilter
@register.filter
def readmore(value, word):
    """Gets an string and searches for the first appearence of the value word.
        returns the string until the argument word
        TODO: Pass various words, if doesn't find the first word, try with the second, and so on
    """
    return value[:value.find(word)]
