from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^/add', 'elementsofrisk.stories.views.add', name='add'),
    url(r'^/search', 'elementsofrisk.stories.views.search', name='search'),
    url(r'^/listpubdate', 'elementsofrisk.stories.views.listpubdate', name='listpub date'),
    url(r'^/listauth', 'elementsofrisk.stories.views.listauth', name='listauth'),
    url(r'^/rand', 'elementsofrisk.stories.views.rand', name='Random'),
)