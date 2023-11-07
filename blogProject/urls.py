from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registation/', user_views.register, name="register"),
    path('profile/', user_views.profile, name="profile"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('', include('blog.urls'))
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# img upload code 
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development