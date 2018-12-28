"""aitoubiao_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
import django
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import staticfiles

from App import views

urlpatterns = [
    url(r'^home/', views.home),
    url(r'^register/', views.register),
    url(r'^login/', views.login),
    url(r'^unlogin/', views.unlogin),
    url(r'^home_model/', views.home_model),
    url(r'^change_nickname/', views.change_nickname),
    url(r'^change_pwd/', views.change_pwd),
    url(r'^change_usericon/', views.change_usericon),
    url(r'^tests/', views.tests,name='test'),
    url(r'^web_name/', views.web_name),
    url(r'^send_announce/', views.send_announce),
    url(r'^send_industry/', views.send_industry),
    url(r'^send_analyse/', views.send_analyse),
    url(r'^web_home/', views.web_home),
    url(r'^save_icon/', views.save_icon,name='save_icon'),
    url(r'^test_img/', views.test_img),
    url(r'^home_each/', views.home_each),
    url(r'^get_announce/', views.get_announce),
    url(r'^get_industry/', views.get_industry),
    url(r'^get_analyse/', views.get_analyse),
    url(r'^web_guide/', views.web_guide),
    url(r'^send_message/', views.send_message),
    url(r'^get_news_info/', views.get_news_info),

]
