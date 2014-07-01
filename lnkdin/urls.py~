from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',url(r'^$', 'lnk2.views.home'),url(r'^login/?$', 'lnk2.views.oauth_login'),
url(r'^logout/?$', 'lnk2.views.oauth_logout'),
url(r'^login/authenticated/?$', 'lnk2.views.oauth_authenticated'),
    # Examples:
    # url(r'^$', 'lnkdin.views.home', name='home'),
    # url(r'^lnkdin/', include('lnkdin.foo.urls')),
      
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

