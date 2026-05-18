from django.contrib import admin
from django.urls import path, include
from articles.views import health_check, trigger_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('articles.urls')),
    path('health/', health_check),
    path('error/', trigger_error),
]