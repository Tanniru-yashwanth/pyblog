from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from pybasic.models import Comment, Questions


def register(request):
    """
    view function to return registration form
    """
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("pybasic:index")
    context = {"form": form}
    return render(request, "users/register.html", context)


def info(request, user_id):
    """
    view function to display user information, comments and questions by user
    """
    user = User.objects.get(id=user_id)
    comments = Comment.objects.filter(user_id=user_id)
    questions = Questions.objects.filter(user_id=user_id)
    context = {'user': user, 'comments': comments, 'questions': questions}
    return render(request, 'users/info.html', context)
