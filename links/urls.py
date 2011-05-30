from django.conf.urls.defaults import *
from links.views import *
from models import Link

urlpatterns = patterns('',
  url(r'^new/$', new),
  url(r'^add/$', add),
  url(r'^$', list),
  url(r'^(?P<id>\d+)/$', view),
  url(r'^(?P<id>\d+)/edit/$', edit),
  url(r'^(?P<id>\d+)/update/$', update),
  url(r'^(?P<id>\d+)/delete/$', delete),
)