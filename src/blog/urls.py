from django.urls import path

from .views import home,about,post_detail

urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('detail/<int:post_id>/',post_detail,name='detail'),





]
