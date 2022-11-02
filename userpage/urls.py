from django.urls import path
from . import views

app_name = 'userpage'

urlpatterns = [
    path('<int:pk>', views.userpage, name='userpage'),
]