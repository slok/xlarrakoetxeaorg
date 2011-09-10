from django.contrib import admin
from mysite.blog.models import Entry

class AdminEntry(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    list_display = ('title', 'pub_date', 'status', 'author', 'mod_date')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'body']
    
admin.site.register(Entry, AdminEntry)
