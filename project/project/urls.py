from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bank/', include('bankapp.urls')),
    path('admin/', admin.site.urls),
]
