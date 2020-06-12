"""lms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from accounts import views as account_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('customers', include('customers.urls')),
    path('vehicles', include('vehicles.urls')),
    path('services', include('services.urls')),
    path('orders', include('orders.urls')),
    path('login/', account_view.login, name="login"),
    path('logout/', account_view.logout, name="logout"),
    path('settings/', account_view.settings, name="settings"),
    path('error/delete', account_view.deleteError, name="deleteError"),
    path('notifications', account_view.notifications, name="notifications"),
    path('notifications/list', account_view.notify, name="notify"),
    path('notifications/update', account_view.makeSeen, name="makeSeen"),




] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
