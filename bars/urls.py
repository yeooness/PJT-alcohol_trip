from django.urls import path
from . import views

app_name = 'bars'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/review/', views.review, name='review'),
    path('<int:pk>/comment', views.comment, name='comment'),
    path('<int:pk>/like', views.like, name='like'),
] 