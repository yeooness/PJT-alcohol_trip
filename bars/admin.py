from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Review, Restaurant, Comment

admin.site.register(Review)
admin.site.register(Restaurant)
admin.site.register(Comment)