from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('', include('django_prometheus.urls')),
    path(r'ht/', include('health_check.urls')),
]
