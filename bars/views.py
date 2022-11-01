from django.shortcuts import render, redirect


def index(request):
    return render(request, "bars/index.html")


def detail(request):
    return render(request, "bars/detail.html")


def review(request):
    return render(request, "bars/review.html")


def update(request):
    return redirect("bars:review")


def delete(request):
    return redirect("bars:detail")


def comment(request):
    return render(request, "bars/comment.html")


def like(request):
    return render(request, "bars/like.html")
