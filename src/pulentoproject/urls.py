"""
URL configuration for pulentoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from api import views, endpoints 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Ruta raíz
    re_path(r'^api/$', views.api_greet),
    re_path(r'^api/teachers$', endpoints.get_teachers),
    re_path(r'^api/teachers/details/(?P<pk>\d{1,5})$', endpoints.get_teacher),
    re_path(r'^api/teachers/delete/(?P<pk>\d{1,5})$', endpoints.delete_teacher),
    re_path(r'^api/courses$', endpoints.get_courses),
    re_path(r'^api/courses/details/(?P<pk>\d{1,5})$', endpoints.get_course),
    re_path(r'^api/courses/delete/(?P<pk>\d{1,5})$', endpoints.delete_course),
    re_path(r'^api/reviews$', endpoints.get_reviews),
    re_path(r'^api/reviews/details/(?P<pk>\d{1,5})$', endpoints.get_review),
    re_path(r'^api/reviews/create$', endpoints.create_review),
    re_path(r'^api/reviews/update/(?P<pk>\d{1,5})$', endpoints.update_review),
    re_path(r'^api/reviews/delete/(?P<pk>\d{1,5})$', endpoints.delete_review),
    re_path(r'^api/users$', endpoints.get_users),
    re_path(r'^api/users/details/(?P<pk>\d{1,5})$', endpoints.get_user),
    re_path(r'^api/users/update/(?P<pk>\d{1,5})$', endpoints.update_user),
    re_path(r'^api/users/delete/(?P<pk>\d{1,5})$', endpoints.delete_user),
    path('register/', views.register, name='register'),
    path('register_superuser/', views.register_superuser, name='register_superuser'),
    path('activate/<str:uidb64>/<str:token>/', views.activate_account, name='activate'),
    path('test-email-verification/', views.test_email_verification, name='test_email_verification'),
    path('login/', views.login_view, name='login'),
]
