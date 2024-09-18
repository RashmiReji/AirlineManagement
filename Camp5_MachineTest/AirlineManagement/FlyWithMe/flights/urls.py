from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('flights/list/', views.flight_list, name='flight_list'),
    path('flights/search/', views.flight_search, name='flight_search'),
    path('flights/add/', views.flight_add, name='flight_add'),
    path('flights/edit/<int:flight_id>/', views.flight_edit, name='flight_edit'),
]
