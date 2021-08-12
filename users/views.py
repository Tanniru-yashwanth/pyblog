from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from pybasic.layer import filter_comments_by_user_id, filter_questions_user_id, get_user_in_detail


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
    user = get_user_in_detail(user_id=user_id)
    comments = filter_comments_by_user_id(user_id=user_id)
    questions = filter_questions_user_id(user_id=user_id)
    context = {'user': user, 'comments': comments, 'questions': questions}
    return render(request, 'users/info.html', context)
