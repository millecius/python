from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from blog import forms
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.BlogIndex, name="index"),
    url(r'^logout/$', views.LogoutView.as_view()),
    url(r'^login/$', login_required(TemplateView.as_view(template_name='login.html'))),
    url(r'^home/$', views.BlogHome, name="home"),
    url(r'^comment/$', views.BlogComment, name="comment"),
    url(r'^game/(?P<pk>[0-9]+)/$', views.BlogGame, name="gameindex"),
    url(r'^game/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$', views.Game, name='gamedetails'),
    url(r'^about/$', views.BlogAbout, name="about"),
    url(r'^login/$', views.BlogLogin, name="login"),
]