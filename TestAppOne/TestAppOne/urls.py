from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('WebApp.app_urls')),
    path('admin/', admin.site.urls),
]
