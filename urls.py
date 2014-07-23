from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import RedirectView


urlpatterns = patterns('',

    url(r'^$', 'seam.views.index', name='index'),
    url(r'^computer/$', 'seam.views.computer', name='computer'),
    
    url(r'^post/(?P<slug>[-\w]+)/$', 'seam.views.detail', name='detail'),

    # Redirect old post structure
    url(r'^(?P<year>\d\d\d\d)/(?P<month>\d\d)/(?P<day>\d\d)/(?P<slug>[-\w]+)/$', RedirectView.as_view(url='/post/%(slug)s/')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
  
urlpatterns += staticfiles_urlpatterns()
