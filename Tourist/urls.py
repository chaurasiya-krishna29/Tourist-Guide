"""
URL configuration for Tourist project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
path('admin/', admin.site.urls),
path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# from django.contrib import admin
# from django.urls import path
# from home.views import *
# from django.conf.urls.static import static
# from django.conf import settings
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns



# from home import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('contact/', views.contact, name='contact'),
#     path('login/', views.login_page, name='login'),
#     path('signup/', views.signup_page, name='signup'),
#     path('index/', views.index, name='index'),
#     path('logout/', views.logout_page, name='logout'),
#     path('verify-email/<uuid:token>/', views.verify_email, name='verify_email'),
#     path('password-reset/', views.password_reset_request, name='password_reset'),
#     path('password-reset/<str:token>/', views.password_reset_confirm, name='password_reset_confirm'),
#     path('profile/', views.profile, name='profile'),
#     path('about/', views.about, name='about'),
#     path('explore/', views.explore, name='explore'),
#     # path('destinations/', views.destinations, name='destinations'),
# ]