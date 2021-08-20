from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User
from pybasic.models import Topic, Entry, TagTopics, Tags


class ViewsTest(TestCase):
    """
    Class to write unit tests for the views.
    """

    def setUp(self):
        """
        Set up function to create objects to use in unit tests.
        """
        self.user = User.objects.create_user(username='sai', password='password')
        self.topic = Topic.objects.create(name='decorator')
        self.entry = Entry.objects.create(topic=self.topic, entry='Adding the functionality to the existing function')
        self.tag = Tags.objects.create(tag='decorators')
        self.client.login(username='sai', password='password')

    def test_index_view(self):
        """
        Function to test the index view function is rendering the correct page.
        """
        url = reverse('pybasic:index')
        response = self.client.get(url)
        html = response.content.decode('utf8')
        self.assertIn('<title>pyblog</title>', html)
        self.assertTemplateUsed(response, 'pybasic/index.html')

    def test_topics_view(self):
        """
        Function to test the topics view function is rendering the correct page.
        """
        url = reverse('pybasic:topics')
        response = self.client.get(url)
        html = response.content.decode('utf8')
        self.assertIn('<title>Topics</title>', html)
        self.assertTemplateUsed(response, 'pybasic/topics.html')

    def test_topic_detail_view(self):
        """
            Function to test the topic detail view function is rendering the correct page.
        """
        url = reverse('pybasic:topic-detail', kwargs={'topic_id': self.topic.id})
        response = self.client.get(url)
        html = response.content.decode('utf8')
        self.assertIn('<title>TopicDetail</title>', html)
        self.assertTemplateUsed(response, 'pybasic/topic_detail.html')

    def test_tag_view(self):
        """
            Function to test the  view function is rendering the correct page.
        """
        url = reverse('pybasic:add-tag')
        response = self.client.get(url)
        html = response.content.decode('utf8')
        self.assertIn('<title>Add Tags</title>', html)
        self.assertTemplateUsed(response, 'pybasic/tag.html')

    def test_comment_view(self):
        """
        Function to test the comment view function is rendering the same page.
        """
        url = reverse('pybasic:comment', kwargs={'topic_id': self.topic.id})
        response = self.client.get(url)
        html = response.content.decode('utf8')
        self.assertIn('<title>Comment</title>', html)
        self.assertTemplateUsed(response, 'pybasic/comment.html')

    def test_question_view(self):
        """
            Function to test the comment view function is rendering the same page.
        """
        url = reverse('pybasic:question', kwargs={'topic_id': self.topic.id})
        response = self.client.get(url)
        html = response.content.decode('utf8')
        self.assertIn('<title>Ask</title>', html)
        self.assertTemplateUsed(response, 'pybasic/question.html')