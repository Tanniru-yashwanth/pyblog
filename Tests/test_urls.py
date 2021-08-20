from django.test import TestCase
from django.contrib.auth.models import User
from pybasic.models import Topic, Entry, TagTopics, Tags
from django.urls import resolve, reverse
from pybasic import views


class UrlsTest(TestCase):
    """
    Class to write unit tests for checking the urls is working correctly.
    """

    def setUp(self):
        self.user = User.objects.create_user(username='sai', password='password')
        self.topic = Topic.objects.create(name='decorator')
        self.entry = Entry.objects.create(topic=self.topic, entry='Adding the functionality to the existing function')
        self.tag = Tags.objects.create(tag='decorators')
        self.client.login(username='sai', password='password')

    def test_home_url(self):
        """
        Function to check the home url is working.
        """
        url = reverse('pybasic:index')
        found = resolve(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(found.func, views.index)

    def test_topics_url(self):
        """
            Function to check the topics url is working.
        """
        url = reverse('pybasic:topics')
        found = resolve(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(found.func, views.topics)

    def test_topic_detail_url(self):
        """
            Function to check the topic detail url is working.
        """
        url = reverse('pybasic:topic-detail', kwargs={'topic_id': self.topic.id})
        response = self.client.get(url)
        found = resolve(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(found.func, views.topic_detail)

    def test_tag_url(self):
        """
            Function to check the tags url is working.
        """
        url = reverse('pybasic:tag-topics', kwargs={'tag_id': self.tag.id})
        found = resolve(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(found.func, views.tag_topics)

    def test_comment_url(self):
        """
            Function to check the comment url is working.
        """
        url = reverse('pybasic:comment', kwargs={'topic_id': self.topic.id})
        found = resolve(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(found.func, views.comment)

    def test_ask_url(self):
        """
            Function to check the ask url is working.
        """
        url = reverse('pybasic:question', kwargs={'topic_id': self.topic.id})
        found = resolve(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(found.func, views.question)

    def test_add_tag(self):
        """
            Function to check the adding tag url is working.
        """
        url = reverse('pybasic:add-tag')
        found = resolve(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(found.func, views.tag)

    def test_add_tag_topic(self):
        """
        Function to check the adding the tag to the topic is working or not.
        """
        url = reverse('pybasic:add-tag-topic', kwargs={'topic_id': self.topic.id})
        found = resolve(url)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(found.func, views.add_tag_topic)
