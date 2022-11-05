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
        "<int:restaurant_pk>/review/<int:review_pk>/comment/",
        views.comment_create,
        name="comment_create",
    ),
    path(
        "<int:restaurant_pk>/review/comment/<int:comment_pk>/delete/",
        views.comment_delete,
        name="comment_delete",
    ),
    path("<int:pk>/restaurant_like/", views.restaurant_like, name="restaurant_like"),
    path(
        "<int:restaurant_pk>/<int:review_pk>/review_like/",
        views.review_like,
        name="review_like",
    ),
    path("search/", views.search, name="search"),
    path("<category>/category/", views.category, name="category"),
    path("<region>/region/", views.region, name="region"),
]
