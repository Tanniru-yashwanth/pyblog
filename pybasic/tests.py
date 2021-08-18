from django.test import TestCase
from django.urls import resolve
from pybasic.views import index, topics, topic_detail
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.shortcuts import reverse
from django.contrib.auth.models import User


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page(self):
        found = resolve("/")
        self.assertEqual(found.func, index)

    def test_home_url_return_index_page(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertIn('<title>pyblog</title>', html)
        self.assertTemplateUsed(response, 'pybasic/index.html')


class TopicsPageTest(TestCase):
    def test_topics_url(self):
        found = resolve("/topics/")
        self.assertEqual(found.func, topics)

    def test_topics_url_return_topics_page(self):
        response = self.client.get("/topics/")
        html = response.content.decode('utf8')
        self.assertIn('<title>Topics</title>', html)
        self.assertTemplateUsed(response, 'pybasic/topics.html')


class TopicDetailTest(TestCase):
    def test_topic_detail_url(self):
        url = reverse('pybasic:topic-detail', kwargs={'user_id': 1, 'topic_id': 1})
        found = resolve(url)
        self.assertEqual(found.func, topic_detail)


class LoginTest(TestCase):
    def test_login_redirects(self):
        response = self.client.post('/users/login', {'username': 'yashwanth', 'password': 'Tanniru@07'})
        self.assertEqual(response.status_code, 301)
