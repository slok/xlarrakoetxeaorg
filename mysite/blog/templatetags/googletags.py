# -*- coding: utf-8 -*-
from django import template
from mysite.blog.models import Entry


register = template.Library()

@register.simple_tag
def plus_one_button(button_type=''):
    
    button_avaiable_types = ('small', '', 'medium', 'tall')
    
    if button_type not in button_avaiable_types:
        button_type = ''
    
    js_button= '''
    <section class="google-plusone-button">
        <script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>
        <g:plusone size="%s"></g:plusone>
    </section>
    ''' % (button_type)
    
    return js_button
 
