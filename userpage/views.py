from django.shortcuts import render

def userpage(request, pk):
    return render(request, 'userpage/userpage.html')