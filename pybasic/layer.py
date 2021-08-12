from .models import Topic, Entry, Comment, Questions
from django.contrib.auth.models import User


def get_user_in_detail(user_id):
    """
    function to get user in detail
    """
    user = User.objects.get(id=user_id)
    return user


def get_all_topics():
    """
    function to get all topics
    """
    topics = Topic.objects.all()
    return topics


def order_topics_by(field="created"):
    """
    function to get all topics in order by date
    """
    topics = get_all_topics()
    return topics.order_by(field)


def topic_in_detail(topic_id):
    """
    function to get single topic in detail
    """
    topic = Topic.objects.get(id=topic_id)
    return topic


def get_all_entries():
    """
    function to get all entries
    """
    entries = Entry.objects.all()
    return entries


def filter_entries_by_topic(topic_id):
    """
    function to get filtered entries by topic
    """
    entries = Entry.objects.filter(topic_id=topic_id)
    return entries


def get_all_comments():
    """
    function to get all comments
    """
    comments = Comment.objects.all()
    return comments


def filter_comments_by_user_id(user_id):
    """
    function to get filtered comments by user field
    """
    comments = Comment.objects.filter(user_id=user_id)


def filter_comments_by_user_id_and_topic_id(user_id, topic_id):
    """
    function to get filtered comments by user and topic fields
    """
    comments = Comment.objects.filter(user_id=user_id, topic_id=topic_id)
    return comments


def get_all_questions():
    """
    function to get all questions
    """
    questions = Questions.objects.all()
    return questions


def filter_questions_user_id(user_id):
    """
    function to get filtered questions by user field
    """
    questions = Questions.objects.filter(user_id=user_id)


def filter_questions_by_topic_id_and_user_id(user_id, topic_id):
    """
    function to get filtered questions by user and topic field
    """
    questions = Questions.objects.filter(user_id=user_id, topic_id=topic_id)
    return questions
