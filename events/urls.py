from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^/request', 'elementsofrisk.events.views.request', name='request'),
    url(r'^/response', 'elementsofrisk.events.views.response', name='response'),
    url(r'^/view', 'elementsofrisk.events.views.view', name='view'),
    url(r'^/viewlist', 'elementsofrisk.events.views.viewlist', name='viewlist'),
    url(r'^/viewajax', 'elementsofrisk.events.views.viewajax', name='ajax'),

)