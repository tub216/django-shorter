"""URLs for the ``django-tinylinks`` app."""
from django.conf.urls import patterns, url, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from tinylinks.views import (
    StatisticsView,
    TinylinkCreateView,
    TinylinkDeleteView,
    TinylinkListView,
    TinylinkRedirectView,
    TinylinkUpdateView,
    TinylinkViewSet,
    UserViewSet,
    db_stats,
    stats,
    tinylink_stats,
    tinylink_expand,
)

# Create router and register our API viewsets with it.
router = DefaultRouter()
router.register(r'tinylinks', TinylinkViewSet)
router.register(r'users', UserViewSet)


urlpatterns = patterns(
    '',
    url(
        r'^$',
        TinylinkListView.as_view(),
        name='tinylink_list'
    ),

    url(
        r'^create/$',
        TinylinkCreateView.as_view(),
        name='tinylink_create'
    ),

    url(
        r'^update/(?P<pk>\d+)/(?P<mode>[a-z-]+)/$',
        TinylinkUpdateView.as_view(),
        name='tinylink_update',
    ),

    url(
        r'^delete/(?P<pk>\d+)/$',
        TinylinkDeleteView.as_view(),
        name='tinylink_delete',
    ),

    url(
        r'^404/$',
        TemplateView.as_view(template_name='tinylinks/notfound.html'),
        name='tinylink_notfound',
    ),

    url(
        r'^statistics/?$',
        StatisticsView.as_view(),
        name='tinylink_statistics',
    ),

    url(
        r'^(?P<short_url>[a-zA-Z0-9-]+)/?$',
        TinylinkRedirectView.as_view(),
        name='tinylink_redirect',
    ),

    url(
        r'^api/',
        include(router.urls),
    ),

    url(
        r'^auth/',
        include('rest_framework.urls', namespace='rest_framework'),
    ),

    url(
        r'^api/db-stats/$',
        db_stats,
        name='api_db_stats'
    ),

    url(
        r'^api/stats/$',
        stats,
        name='api_stats'
    ),

    url(
        r'^api/url-stats/(?P<short_url>\w+)/',
        tinylink_stats,
        name='api_url_stats'
    ),

    url(
        r'^api/url-stats/',
        tinylink_stats,
        name='api_url_stats'
    ),

    url(
        r'^api/expand/(?P<short_url>\w+)/',
        tinylink_expand,
        name='api_tinylink_expand'
    ),

    url(
        r'^api/expand/',
        tinylink_expand,
        name='api_tinylink_expand'
    ),
)
