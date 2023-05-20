"""
URL configuration for myblooddonationdepot project.

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
"""
URL configuration for mybloodbankdepot project.

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
from django.urls import path
from bloodbankapp import views
from django.contrib.auth.views import LogoutView, LoginView


urlpatterns = [
    path('index/', views.index, name='index'),
    path('adminclick', views.adminclick_view, name='adminclick'),
    path('', LoginView.as_view(template_name='admin/login.html'), name='adminlogin'),
    path('afterlogin', views.afterlogin_view, name='afterlogin'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin-dashboard', views.admin_dashboard_view, name='admin-dashboard'),
    path('Registration', views.Registration, name='Registration'),
    path('admin/404', views.admin_404, name='admin-404'),
    path('admin-contact', views.admin_contact_view, name='admin-contact'),
    path('admin-contact/', views.admin_contact, name='admin_contact'),
    path('registration', views.registration, name='registration'),
    path('', views.registration_success, name='registration_success'),
    path('admin/contact/delete/<int:registration_id>/', views.delete_registration, name='delete-registration'),
    path('admin-contact/edit/<int:registration_id>/', views.edit_registration_view, name='edit-registration'),

]
