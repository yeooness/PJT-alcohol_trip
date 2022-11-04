from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.http import JsonResponse
from .models import User
import json

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("bars:index")
    else:
        form = AuthenticationForm()
    context = {
        "form": form,
    }
    return render(request, "accounts/login.html", context)

def logout(request):
    auth_logout(request)
    return redirect("bars:index")

def naver_callback(request):
    return render(request, 'accounts/naver_callback.html')

def userpage(request, pk):
    request_user = User.objects.get(pk=pk)
    profile_image = request_user.profile_image
    username = request_user.username
    context = {
        'request_user': request_user,
        'profile_image': profile_image,
        'username': username,
    }
    return render(request, 'accounts/userpage.html', context)

def follow(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(pk=pk)
        print(user.pk)
        print(user)
        if user != request.user:
            if user.followers.filter(pk=request.user.pk).exists():
                user.followers.remove(request.user)
                is_followed = False
            else:
                user.followers.add(request.user)
                is_followed = True
            print("팔로우됨?")
            print(is_followed)
            context = {
                'is_followed': is_followed,
                'followers_count': user.followers.count(),
                'followings_count': user.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:userpage', user.username)
    return redirect('accounts:login')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bars:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def id_check(request):
    print(666666666666666666666666666)
    jsonObject = json.loads(request.body)
    # user = User()
    username = jsonObject.get('username')
    print(111111111111111111111111)
    username = "k" + str(username)
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
    else:
        username = jsonObject.get('username')
        email = jsonObject.get('email')
        profile_image = jsonObject.get('profile_image')
        user = User.objects.create(username=username, email=email, profile_image=profile_image)
        user.save()
    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    print('아아아아')
    return JsonResponse({'username': user.username, 'email': user.email})

def id_check_naver(request):
    jsonObject = json.loads(request.body)
    # user = User()
    username = jsonObject.get('id')
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
    else:
        username = "n" + str(username)
        email = jsonObject.get('email')
        profile_image = jsonObject.get('profile_image')
        user = User.objects.create(username=username, email=email, profile_image=profile_image)
        user.save()
    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    print('아아아아')
    return JsonResponse({'username': user.username, 'email': user.email, 'profile_image':profile_image})