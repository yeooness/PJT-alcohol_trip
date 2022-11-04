from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('<int:pk>/', views.userpage, name='userpage'),
    path('login/naver_callback/', views.naver_callback, name='naver_callback'),
    path('id_check/', views.id_check, name='id_check'),
]