from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('polls.urls')),
    path('api/v1/openapi/', get_schema_view(
        title="Polls",
        description="API for polls",
        version="1.0.0"
    ), name='openapi-schema'),
]

