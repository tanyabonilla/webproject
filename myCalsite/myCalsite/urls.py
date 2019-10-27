from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('myCalapp.urls')),
        #path('ProfilePage/', include('myCalapp.urls')),
        #path('/helloworld', include('a02.urls')),
]
