from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path(
        "/doc/schema/download/",
        SpectacularAPIView.as_view(),
        name="schema-download",
    ),
    path(
        "/doc/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "/docschema/redoc-ui/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc-ui",
    ),
]
