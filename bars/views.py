from gzip import READ
from django.shortcuts import render, redirect
from .forms import ReviewForm, CommentForm
from .models import Restaurant, Review, Comment
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


def index(request):
    restaurants = Restaurant.objects.all()
    context = {
        "restaurants": restaurants,
    }
    return render(request, "bars/index.html", context)


def detail(request, restaurant_pk):
    restaurant = Restaurant.objects.get(pk=restaurant_pk)
    review = request.POST.get("review")
    reviews = Review.objects.filter(restaurant_id=restaurant_pk)
    comments = Comment.objects.filter(review_id=review)
    comment_form = CommentForm
    context = {
        "restaurant": restaurant,
        "reviews": reviews,
        "comment_form": comment_form,
        # "comments": reviews.comment_set.all(),
        "comments": comments,
    }
    return render(request, "bars/detail.html", context)


@login_required
def review(request, pk):
    if request.method == "POST":
        review_form = ReviewForm(request.POST, request.FILES)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.restaurant_id = pk
            review.save()
            return redirect("bars:detail", pk)
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "bars/review.html", context)


def update(request, restaurant_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        review_form = ReviewForm(request.POST, instance=review)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.restaurant_id = restaurant_pk
            review.save()
            return redirect("bars:detail", restaurant_pk)
    else:
        review_form = ReviewForm(instance=review)
    context = {
        "review_form": review_form,
    }
    return render(request, "bars/update.html", context)


def delete(request, restaurant_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
        return redirect("bars:detail", restaurant_pk)
    else:
        return HttpResponseForbidden


def comment_create(request, restaurant_pk):
    review = request.POST.get("review")
    review_pk = Review.objects.get(pk=review)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review_pk
        comment.user_id = request.user.pk
        comment.save()
    return redirect("bars:detail", restaurant_pk)


def like(request, pk):
    restaurant = Restaurant.objects.get(pk=pk)
    if request.user in restaurant.like_users.all():
        restaurant.like_users.remove(request.user)
        # is_liked = False
    else:
        restaurant.like_users.add(request.user)
        # is_liked = True
    return redirect("bars:detail", pk)
