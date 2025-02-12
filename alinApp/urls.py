from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('panel-admin/', admin.site.urls),
    path("", include ('sharingApp.urls')),
    path("",include('django.contrib.auth.urls')),
]
