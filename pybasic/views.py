from django.shortcuts import render, redirect
from .forms import QuestionForm, CommentFormDisplay
from django.http import HttpResponse
from django.contrib import messages
from .layer import (
    get_all_topics,
    topic_in_detail,
    get_user_in_detail,
    get_all_entries,
    get_all_comments,
    get_all_questions,
    filter_entries_by_topic,
    filter_comments_by_user_id_and_topic_id,
    filter_questions_by_topic_id_and_user_id,
    order_topics_by
)


def index(request):
    """
    function to return index page for the request
    """
    return render(request, "pybasic/index.html")


def topics(request):
    """
    function to return topics page
    """
    topics_ = get_all_topics()
    context = {'topics_': topics_}
    return render(request, "pybasic/topics.html", context)


def topic_detail(request, user_id, topic_id):
    """
    function to return each topic in detail and provides comment forms and ask forms
    """
    topic = topic_in_detail(topic_id)
    user = get_user_in_detail(user_id)
    entries = filter_entries_by_topic(topic_id)
    comments = filter_comments_by_user_id_and_topic_id(user_id, topic_id)
    questions = filter_questions_by_topic_id_and_user_id(user_id, topic_id)
    if request.method != "POST":
        form = CommentFormDisplay()
        form_1 = QuestionForm()

    else:
        form = CommentFormDisplay(data=request.POST)
        form_1 = QuestionForm(data=request.POST)
        if "comment" in form.data:
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.topic = topic
                instance.save()
                messages.info(request, "comment was added")
                return redirect("pybasic:topic-detail", user.id, topic.id)
            else:
                HttpResponse("U have entered the wrong input")
        elif "question" in form_1.data:
            if form_1.is_valid():
                instance = form_1.save(commit=False)
                instance.user = request.user
                instance.topic = topic
                instance.save()
                return redirect("pybasic:topic-detail", user.id, topic.id)
            else:
                HttpResponse("U have entered the wrong input")

    context = {
        "entries": entries,
        "topic": topic,
        "form": form,
        "form_1": form_1,
        "user": user,
        "comments": comments,
        "questions": questions,
    }
    return render(request, "pybasic/topic_detail.html", context)
