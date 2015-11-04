from django.conf.urls import include, url
from views import AuthorDetailView
from views import AuthorListView

urlpatterns = [
    url(r'^authors/$', AuthorListView.as_view(), name='author-list'),
    url(r'^authors/(?P<pk>\d+)/$', AuthorDetailView.as_view(), name='author-detail'),
]