from django.contrib import admin
from django.urls import include, path
from accounts.views import MyLogoutView
from django.contrib.auth import views as auth_views
from accounts.views import logout, login, signup 
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home.html', views.home, name='home_html'),
    path('p_messages/', include('p_messages.urls', namespace='p_messages')),
    path('logout/', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
]
