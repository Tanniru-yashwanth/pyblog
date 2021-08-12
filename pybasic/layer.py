from .models import Topic, Entry
from django.contrib.auth.models import User


def get_topics():
    topics = Topic.objects.order_by("created")
    context = {"topics": topics}
    return context


def topic_in_detail(topic_id):
    topic = Topic.objects.get(id=topic_id)
    return topic


def get_user(user_id):
    user = User.objects.get(id=user_id)
    return user


def get_entries(topic_id):
    topic_ = topic_in_detail(topic_id)
    entries = Entry.objects.filter(topic_id=topic_id).order_by("-created")
    return entries
