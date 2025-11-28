from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', views.index, name='index'),
    path('vn/<int:dt>/', views.vn_detail, name='VN_detailpage'),
    path('login/', views.login_view, name='login'),
    path('Home/', views.home, name='Home'),  # requires login
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('review/delete/<int:review_id>/', views.delete_review, name='delete_review')
]