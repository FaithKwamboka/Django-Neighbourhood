from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('all-hoods/', views.hoods, name='hood'),
    path('new-hood/', views.create_hood, name='new-hood'),
    path('<hood_id>/members', views.hood_members, name='members'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
]