from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = \
    [
        path('', views.index, name='index'),
        path('login/', views.login, name='login'),
        path('new_user/', views.new_user, name='new_user'),
        path('<str:username>/', views.user_page, name='user_page'),
        path('<str:username>/<str:contact_name>/', views.contact_display, name='contact_display')
    ]