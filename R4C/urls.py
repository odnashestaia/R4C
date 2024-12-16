from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robot/', include('robots.urls')),
    path('orders/', include('orders.urls')),
]
