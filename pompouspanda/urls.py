from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

(r'^$', 'pompouspanda.blog.views.index'),
url(
    r'^blog/view/(?P<slug>[^\.]+).html', 
    'pompouspanda.blog.views.view_post', 
    name='view_blog_post'),
url(
    r'^blog/category/(?P<slug>[^\.]+).html', 
    'pompouspanda.blog.views.view_category', 
    name='view_blog_category'),






#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pompouspanda.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', 'blog.views.index'),
#    url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post'),
#)
