from django.shortcuts import render, redirect
from .models import Restaurant, Review, Comment

def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        'restaurants' : restaurants,
    }
    return render(request, "bars/index.html", context)


def detail(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    context = {
        'restaurant' : restaurant,
    }
    return render(request, "bars/detail.html", context)


def review(request):
    return render(request, "bars/review.html")


def update(request):
    return redirect("bars:review")


def delete(request):
    return redirect("bars:detail")


def comment(request):
    return render(request, "bars/comment.html")


def like(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    if request.user in restaurant.like_users.all():
        restaurant.like_users.remove(request.user)
        # is_liked = False
    else:
        restaurant.like_users.add(request.user)
        # is_liked = True
    return redirect('bars:detail', pk)
