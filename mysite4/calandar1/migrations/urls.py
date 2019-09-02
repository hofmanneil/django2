rom django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('calandar1/',include('calandar1.urls')),
    path('admin/', admin.site.urls),
]
