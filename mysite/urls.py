from django.conf.urls.defaults import patterns, include, url
from mysite import views, blog

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    
    url(r'^$', views.index),
    url(r'^about/$', views.about),
    url(r'^projects/$', views.projects),
    
    # Website blog
    url(r'^blog/', include('blog.urls')),
    
    # Django administration
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),


)
