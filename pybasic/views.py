from django.shortcuts import render, redirect
from .forms import QuestionForm, CommentFormDisplay, TagForm, TagsTopicsForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .service_layer import (
    get_all_topics,
    topic_in_detail,
    filter_entries_by_topic,
    filter_comments_by_user_topic,
    filter_questions_by_topic_user,
    get_all_tags,
    filter_topics_by_tag,
)


def index(request):
    """
    Function to return index page for the request.
    """
    return render(request, "pybasic/index.html")


def topics(request):
    """
    Function to return topics page.
    """
    topics_ = get_all_topics()
    tags = get_all_tags()
    context = {"topics_": topics_, "tags": tags}
    return render(request, "pybasic/topics.html", context)


def topic_detail(request, topic_id):
    """
    Function to return each topic in detail and provides comment form and ask form.
    """
    topic = topic_in_detail(topic_id)
    entries = filter_entries_by_topic(topic_id)
    comments = filter_comments_by_user_topic(request.user.id, topic_id)
    questions = filter_questions_by_topic_user(request.user.id, topic_id)

    context = {
        "topic": topic,
        "entries": entries,
    }
    return render(request, "pybasic/topic_detail.html", context)


@login_required(login_url='/users/login')
def comment(request, topic_id):
    topic = topic_in_detail(topic_id)
    if request.method != "POST":
        form = CommentFormDisplay()
    else:
        form = CommentFormDisplay(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.topic = topic
            instance.user = request.user
            instance.save()
            messages.info(request, "comment was added")
            return redirect("pybasic:topic-detail", topic.id)
        else:
            HttpResponse("U have entered the wrong input")
    context = {"form": form, "topic": topic}
    return render(request, "pybasic/comment.html", context)


@login_required(login_url='/users/login')
def question(request, topic_id):
    topic = topic_in_detail(topic_id)
    if request.method != "POST":
        form_1 = QuestionForm()
    else:
        form_1 = QuestionForm(data=request.POST)
        if form_1.is_valid():
            instance = form_1.save(commit=False)
            instance.user = request.user
            instance.topic = topic
            instance.save()
            messages.info(request, "question was added")
            return redirect("pybasic:topic-detail", topic.id)
        else:
            HttpResponse("You have entered the wrong input")
    context = {
        "form_1": form_1,
        "topic": topic,
    }
    return render(request, "pybasic/question.html", context)


@login_required(login_url='/users/login')
def tag(request):
    if request.method != "POST":
        tag_form = TagForm()
    else:
        tag_form = TagForm(data=request.POST)
        if tag_form.is_valid():
            instance = tag_form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.info(request, "tag was added")
            return redirect("pybasic:topics")
    context = {
        "tag_form": tag_form,
    }
    return render(request, "pybasic/tag.html", context)


@login_required(login_url='/users/login')
def add_tag_topic(request, topic_id):
    topic = topic_in_detail(topic_id)
    if request.method != "POST":
        form = TagsTopicsForm()
    else:
        form = TagsTopicsForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.topic = topic
            instance.save()
            return redirect("pybasic:topic-detail", topic.id)
    context = {"form": form, "topic": topic}
    return render(request, "pybasic/tag_topics.html", context)


def tag_topics(request, tag_id):
    tag_topics_ = filter_topics_by_tag(tag_id=tag_id)
    context = {"tag_topics_": tag_topics_}
    return render(request, "pybasic/tag_topics.html", context)
