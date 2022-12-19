from django.urls import path
from . import views

app_name = "buildmaker"

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('killer_builds/', views.TodoView.as_view(), name='kbuild_list'),
    path('killer_builds/create', views.TodoView.as_view(), name='kbuild_create'),
    path('killer_builds/<int:pk>', views.TodoView.as_view(), name='kbuild_details'),
    path('survivor_builds/', views.TodoView.as_view(), name='sbuild_list'),
    path('survivor_builds/create', views.TodoView.as_view(), name='sbuild_create'),
    path('survivor_builds/<int:pk>', views.TodoView.as_view(), name='sbuilds_details'),
]
