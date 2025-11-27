from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('vn/<int:dt>/', views.vn_detail, name='VN_detailpage'),
    path('login/', views.login_view, name='login'),
    #path('logout/', views.logout_view, name='logout'),
]