from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()
urlpatterns = patterns('',
                        url(r'^$', 'blog.views.index', name='home'),
                        url(r'^admin/', include(admin.site.urls)),
                        url(
                            r'^view/(?P<slug>[^\.]+).html', 
                            'blog.views.view_post', 
                            name='view_blog_post'),
                        url(
                            r'^category/(?P<slug>[^\.]+).html', 
                            'blog.views.view_category', 
                            name='view_blog_category'),
)