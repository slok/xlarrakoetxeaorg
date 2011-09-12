from django.contrib import admin
from mysite.blog.models import Entry

import os
import settings

#enable javascript editor for media
class CommonMedia:
    
    js = (
        'https://ajax.googleapis.com/ajax/libs/dojo/1.6.0/dojo/dojo.xd.js',
        os.path.join(settings.STATIC_URL, 'js/editor.js'),
    )
    css = {
        'all': (os.path.join(settings.STATIC_URL,'css/editor.css'), ),
    }
    
    
class AdminEntry(admin.ModelAdmin):
    
    date_hierarchy = 'pub_date'
    list_display = ('title', 'pub_date', 'status', 'author', 'mod_date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body']

#Set the Dojo editor or not (HTML vs Markdown)
cm = None
if settings.ENABLE_DOJO_EDITOR:
    cm = CommonMedia

admin.site.register(Entry, AdminEntry, Media = cm)


