from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm, CustomUserChangeForm
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
        if user != request.user:
            if user.followers.filter(pk=request.user.pk).exists():
                user.followers.remove(request.user)
                is_followed = False
            else:
                user.followers.add(request.user)
                is_followed = True
            follow_user = user.followers.filter(pk=request.user.pk)
            following_user = user.followings.filter(pk=request.user.pk)
            print(follow_user)
            follow_user_list = []
            following_user_list = []
            for follow in follow_user:
                follow_user_list.append({'pk': follow.pk, 'username': follow.username,})
            for following in following_user:
                following_user_list.append({'pk': following.pk, 'username': following.username,})
            print("팔로우됨?")
            context = {
                'is_followed': is_followed,
                'follow_user': follow_user_list,
                'following_user': following_user_list,
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
    jsonObject = json.loads(request.body)
    # user = User()
    username = jsonObject.get('username')
    username = "k" + str(username)
    print(username)
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        profile_image = jsonObject.get('profile_image')
    else:
        email = jsonObject.get('email')
        profile_image = jsonObject.get('profile_image')
        name = jsonObject.get('nickname')
        user = User.objects.create(username=username, email=email, profile_image=profile_image, name=name, image_string=str(profile_image))
        user.save()
    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    print('아아아아')
    return JsonResponse({'username': user.username, 'email': user.email, 'profile_image':user.profile_image.url, 'name':user.name,})

def id_check_naver(request):
    jsonObject = json.loads(request.body)
    # user = User()
    username = jsonObject.get('id')
    username = "n" + str(username)
    print(username)
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
    else:
        email = jsonObject.get('email')
        profile_image = jsonObject.get('profile_image')
        name = jsonObject.get('name')
        user = User.objects.create(username=username, email=email, profile_image=profile_image, name=name, image_string=str(profile_image))
        user.save()
    auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    print('아아아아')
    return JsonResponse({'username': user.username, 'email': user.email, 'profile_image':user.profile_image.url, 'name':user.name,})

def update(request, pk):
    username = request.user.username
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:userpage', pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
        'username': username,
    }
    return render(request, 'accounts/update.html', context)