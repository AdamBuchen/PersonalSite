#python manage.py runserver 0.0.0.0:8000
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'PersonalSite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'PersonalSiteApp.views.index'),
    url(r'^admin/', include(admin.site.urls)),
)
