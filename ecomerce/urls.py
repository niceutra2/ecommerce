"""ecomerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home.views import *
from django.conf.urls.static import static, serve
from django.conf import settings
from django.contrib.auth import views as auth_view

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
        url(r'^accounts/', include('django.contrib.auth.urls'),),
        url(r'^accounts/login/$', auth_view.LoginView.as_view(template_name="index.html"),name='login'),
        #url(r'^accounts/login/$', auth_view.login, name = "login"),
        url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
        url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),
        url(r'^admin/', admin.site.urls),
        url(r'^home/', HomeView, name='home'),
        url(r'^product/(?P<pk>\d+)', Single_product, name='single_product'),
        url(r'^ckeditor/', include('ckeditor_uploader.urls')),
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
        url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
