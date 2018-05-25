
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, LoginView, LogoutView
from .views import UserCreate, LoginUser

app_name = 'users'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='statistic:index'), name='logout'),
    path('register/', UserCreate.as_view(), name='register'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


