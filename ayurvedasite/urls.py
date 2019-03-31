from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
app_name='ayurvedasite'
urlpatterns=[
path('', views.home_page, name='home_page'),
path('intro/', views.intro_page, name='intro_page'),
path('logout/', auth_views.LogoutView.as_view(template_name='ayurvedasite/home.html'), name='logout'),
path('comment/', views.add_comment, name='add_comment'),
path('symptoms/',views.symptoms,name='symptoms'),


]