from django.contrib import admin
from .models import Restaurant, Review, Comment, Search

admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Search)