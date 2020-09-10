from django.conf import settings
from django.urls import include, path

urlpatterns = [
    path('', include('stats.urls')),
]

if settings.DEBUG is True:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns
