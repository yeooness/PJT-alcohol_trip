from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


class Restaurant(models.Model):
    name = models.CharField(max_length=50)
    category = models.TextField()
    address = models.TextField(null=True)
    phone = models.TextField(null=True)
    map_url = models.TextField(null=True)
    hours = models.TextField(null=True)
    picture1 = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 80},
        null=True
    )
    picture2 = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 80},
        null=True
    )
    picture3 = ProcessedImageField(
        upload_to="images/",
        blank=True,
        processors=[ResizeToFill(1200, 960)],
        format="JPEG",
        options={"quality": 80},
        null=True
    )
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="like_restaurants"
    )
    like_count = models.IntegerField(default=0)


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

class Search(models.Model):
    keyword = models.TextField(max_length=30)
    count = models.IntegerField(default=1)