from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^', include('article.blog.urls', namespace="blog"))
)
