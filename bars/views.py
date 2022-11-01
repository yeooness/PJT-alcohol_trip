from django.shortcuts import render

def index(request):
    return render(request, 'bars/index.html')

def detail(request):
    return render(request, 'bars/detail.html')

def review(request):
    return render(request, 'bars/review.html')

def comment(request):
    return render(request, 'bars/comment.html')

def like(request):
    return render(request, 'bars/like.html')
