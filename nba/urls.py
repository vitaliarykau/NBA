from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('statistic.urls', namespace='statistic')),
    path('users/', include('users.urls', namespace='users')),

]


