"""igs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from re import template
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

from account.views import UserPasswordResetDoneView, UserPasswordResetView, UserPasswordResetConfirmView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls')),
    path('upload/', include('upload.urls')),
    path('grading/', include('grading.urls')),
    path('result/', include('result.urls')),

    path('password_reset/', UserPasswordResetView.as_view(),
        name='password_reset'),

    path('password_reset/done/', UserPasswordResetDoneView.as_view(),
        name='password_reset_done'),

    path('reset/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(
        template_name='password_reset/password_reset_confirm.html'),
        name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset/password_reset_complete.html'),
        name='password_reset_complete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
