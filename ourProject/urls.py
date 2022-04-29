from django.contrib import admin
from django.urls import path, include

from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls')),
    path('signup/', user_views.signup, name='signup' ),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('email-service/', include('email_service.urls')),
    path('chat/', include('chat.urls'))

]


handler404 = 'library.views.not_found_404'
handler500 = 'library.views.server_error_500'
