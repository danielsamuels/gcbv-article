from django.conf.urls import include, url


urlpatterns = [
    url(r'^', include('article.blog.urls', namespace="blog")),
]
