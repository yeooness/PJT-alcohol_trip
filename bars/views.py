from gzip import READ
from django.shortcuts import render, redirect
from .forms import ReviewForm, CommentForm
from .models import Review
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "bars/index.html")


def detail(request):
    return render(request, "bars/detail.html")


@login_required
def review(request):
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect("bars:index")
    else:
        review_form = ReviewForm()
    context = {
        "review_form": review_form,
    }
    return render(request, "bars/review.html", context)


def update(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        if request.method == "POST":
            review_form = ReviewForm(request.POST, instance=review)
            if review_form.is_valid():
                review_form.save()
                return redirect("bars:detail", review.pk)
        else:
            review_form = ReviewForm(instance=review)
        context = {
            "review_form": review_form,
        }
        return render(request, "bars/update.html", context)
    else:
        return HttpResponseForbidden()


def delete(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user == review.user:
        if request.method == "POST":
            review.delete()
            return redirect("bars/index")
    else:
        return HttpResponseForbidden


@login_required
def comment(request, pk):
    review = Review.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
    return redirect("bars:detail", review.pk)


def like(request, pk):
    review = Review.objects.get(pk=pk)
    if request.user in review.like_users.all():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect("bars:detail", pk)
