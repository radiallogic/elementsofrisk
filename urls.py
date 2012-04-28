from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'elementsofrisk.index.views.index', name='index'),
    url(r'^portal', 'elementsofrisk.index.views.portal', name='portal'),
    url(r'^profiles',include('elementsofrisk.profiles.urls') ),
    url(r'^events',include('elementsofrisk.events.urls') ),
    url(r'^stories',include('elementsofrisk.stories.urls') )
)