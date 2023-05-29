from django.urls import path
from app import views

urlpatterns = [
    path('',views.home),
    path('main',views.main),
    path('view',views.view),
    path('base', views.base),
#    path('home', views.home),
    path('delete/<int:id>',views.delete),
    path('edit/<int:id>',views.edit),
    path('edit/update/<int:id>',views.update),
    path('register',views.register),
 #   path('logout',views.logout)




]