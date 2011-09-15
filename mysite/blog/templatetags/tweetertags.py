# -*- coding: utf-8 -*-
from django import template
from mysite.blog.models import Entry


register = template.Library()

@register.simple_tag
def tweet_button(user, button_type, user2=None):
    
    button_avaiable_types = ('vertical', 'horizontal', 'none')
    
    if button_type not in button_avaiable_types:
        button_type = 'horizontal'
    
    if not user2:
        user2=''
    else:
        user2 = 'data-related="' + user2 + '"'

    
    js_button= '''
    <section class="twitter-share-button">
        <a href="https://twitter.com/share" class="twitter-share-button" data-count="%s" 
        data-via="%s" %s data-lang="es">Tweet</a><script type="text/javascript"
         src="//platform.twitter.com/widgets.js"></script>
    </section>
    ''' % (button_type, user, user2)
    
    return js_button
 
