from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic.simple import redirect_to

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', 'seam.views.index', name='index'),
    url(r'^computer/$', 'seam.views.computer', name='computer'),
    
    url(r'^post/(?P<slug>[-\w]+)/$', 'seam.views.detail', name='detail'),

    # Redirect old post structure
    url(r'^(?P<year>\d\d\d\d)/(?P<month>\d\d)/(?P<day>\d\d)/(?P<slug>[-\w]+)/$', redirect_to, {'url': '/post/%(slug)s/'}),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
  
urlpatterns += staticfiles_urlpatterns()
