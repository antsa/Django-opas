from django.conf.urls.defaults import *
from links.views import *
from models import Link

urlpatterns = patterns('',
    url(r'^new/$', new),
    url(r'^add/$', add),
    url(r'^$', list),
    url(r'^(?P\d+)/$', view),
    url(r'^(?P\d+)/edit/$', edit),
    url(r'^(?P\d+)/update/$', update),
    url(r'^(?P\d+)/delete/$', delete),
)