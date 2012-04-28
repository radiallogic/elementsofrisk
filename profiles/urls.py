from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^/login','django.contrib.auth.views.login', {'template_name': 'profiles/Login.html', 'redirect_field_name': 'viewprofile'} ),
    url(r'^/logout', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^/viewprofile', 'elementsofrisk.profiles.views.viewProfile', name='View profile'),
    url(r'^/editprofile', 'elementsofrisk.profiles.views.editProfile', name='editprofile'),
    url(r'^/addfriend', 'elementsofrisk.profiles.views.addFriend', name='addfriend'),
    url(r'^/searchprofiles', 'elementsofrisk.profiles.views.searchProfiles', name='searchprofiles'),
    url(r'^/leavereview', 'elementsofrisk.profiles.views.leaveReview', name='leavereview'),
    url(r'^/register', 'elementsofrisk.profiles.views.register', name='Register'),
    url(r'^/whatnext', 'elementsofrisk.profiles.views.whatNext', name='Whatnext'),
)
