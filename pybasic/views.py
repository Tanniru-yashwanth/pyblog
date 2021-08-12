from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import QuestionForm, CommentFormDisplay
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .layer import get_topics, topic_in_detail, get_user, get_entries


def index(request):
    """
    function to return index page for the request
    """
    return render(request, "pybasic/index.html")


def topics(request):
    """
    function to return topics page
    """
    context = get_topics()
    return render(request, "pybasic/topics.html", context)


def topic_detail(request, user_id, topic_id):
    """
    function to return each topic in detail and provides comment forms and ask forms
    """
    topic = topic_in_detail(topic_id)
    user = get_user(user_id)
    entries = get_entries(topic_id)
    if request.method != "POST":
        form = CommentFormDisplay()
        form_1 = QuestionForm()

    else:
        form = CommentFormDisplay(request.POST)
        form_1 = QuestionForm(data=request.POST)
        if form:
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.topic = topic
                instance.save()
                return redirect("pybasic:topic-detail", user.id, topic.id)
            else:
                HttpResponse("U have entered the wrong input")
        elif form_1:
            if form_1.is_valid():
                instance = form_1.save(commit=False)
                instance.user = request.user
                instance.topic = topic
                instance.save()
                messages.info(request, 'comment was added')
                return redirect("pybasic:topic-detail", user.id, topic.id)
            else:
                HttpResponse("U have entered the wrong input")

    context = {"entries": entries, "topic": topic, 'form': form, 'form_1': form_1, 'user': user}
    return render(request, "pybasic/topic_detail.html", context)


