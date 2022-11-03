from django.urls import path
from . import views

app_name = "bars"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:restaurant_pk>/", views.detail, name="detail"),
    path("<int:pk>/review/", views.review, name="review"),
    path(
        "<int:restaurant_pk>/review/<int:review_pk>/update/",
        views.update,
        name="update",
    ),
    path(
        "<int:restaurant_pk>/review/<int:review_pk>/delete/",
        views.delete,
        name="delete",
    ),
    path(
        "<int:restaurant_pk>/review/comment/",
        views.comment_create,
        name="comment_create",
    ),
    path("<int:pk>/like", views.like, name="like"),
]
