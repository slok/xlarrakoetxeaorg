from django.conf.urls.defaults import patterns, include, url
from mysite import views, blog

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^about/$', views.about),
    url(r'^projects/$', views.projects),
    
    url(r'^blog/', include('blog.urls')),

)
