from django.db import models
from django.contrib.auth.models import User
import django
from tagging.fields import TagField
import datetime

from mysite.blog.managers import PublishedManager


#def _admin_users_in_choices():
#    """
#        gets all the admin users from auth_user
#    """
#    #We need to catch and pass this error because auth_user table isn't created before this and fails when it checks,
#    #the exception thrwon is: "django.db.utils.DatabaseError: no such table: auth_user"
#    try:
#        raw_users = User.objects.all()
#        users = []
#        for i in raw_users:
#            full_name = i.username
#            users.append((full_name, full_name))
#            
#    except django.db.utils.DatabaseError:
#        pass
#        
#    return users

def _get_default_user():
    return User.objects.get(pk=1)


class Entry(models.Model):
    #Choices
    #user_choices = _admin_users_in_choices()
    
    status_choices = (
        ('p', 'Published'),
        ('d', 'Draft'),
        ('w', 'Withdrawn'),
    )
    
    entry_format_choices = (
        ('html', 'HTML'),
        ('md', 'Markdown'),
        ('rst', 'reStructuredText'),
    )
    #Model
    title = models.CharField('title', max_length=200)
    body = models.TextField()
    slug = models.SlugField('slug', unique_for_date='pub_date')
    #author = models.CharField(max_length=30, choices=user_choices)
    author = models.ForeignKey(User, default=_get_default_user)
    #pub_date = models.DateTimeField('Date published', auto_now_add=True)
    pub_date = models.DateTimeField('Date published', default=datetime.datetime.now) #if we want to publish in the future we need to put the date "manually"
    mod_date =  models.DateTimeField('Date modified', auto_now=True)
    tags = TagField()
    status =  models.CharField(max_length=1, choices=status_choices, default='d')
    allow_comments = models.BooleanField(default=True)
    entry_format = models.CharField(max_length=30, choices=entry_format_choices, default='md')
    
    #Manager with filter and default
    objects = models.Manager()
    published_objects = PublishedManager()

    def __unicode__(self):
        return u'%s' % self.title

            
