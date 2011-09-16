# -*- coding: utf-8 -*-
from django import template
from mysite.blog.models import Entry
import settings

register = template.Library()

@register.simple_tag
def tweet_button(button_type, url=None):
    
    button_avaiable_types = ('vertical', 'horizontal', 'none')
    
    if button_type not in button_avaiable_types:
        button_type = 'horizontal'
    
    
    if len(settings.TWITTER_BUTTON_ACCOUNTS) < 2:
        user = settings.TWITTER_BUTTON_ACCOUNTS[0]
        user2 = ''
    else:
        user1 = settings.TWITTER_BUTTON_ACCOUNTS[0]
        user2 = settings.TWITTER_BUTTON_ACCOUNTS[1]
        user2 = 'data-related="' + user2 + '"'

    if url:
        url = 'data-url="' + url + '"'
    else:
        url = ''
    
    js_button= '''
    <section class="twitter-share-button">
        <a href="https://twitter.com/share" class="twitter-share-button" %s data-count="%s" 
        data-via="%s" %s data-lang="es">Tweet</a><script type="text/javascript"
         src="//platform.twitter.com/widgets.js"></script>
    </section>
    ''' % (url, button_type, user, user2)
    
    return js_button
 
