from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    hours = models.TimeField()
    parking = models.BooleanField()
    contact = models.CharField(max_length=30)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 80},
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_restaurants"
    )


class Review(models.Model):
    grade_choices = (
        ("1", "⭐"),
        ("2", "⭐⭐"),
        ("3", "⭐⭐⭐"),
        ("4", "⭐⭐⭐⭐"),
        ("5", "⭐⭐⭐⭐⭐"),
    )
    title = models.CharField(max_length=50)
    content = models.TextField()
    grade = models.CharField(max_length=2, choices=grade_choices)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 80},
    )
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, blank=True)
    like_usersreview = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_review"
    )


class Comment(models.Model):
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
