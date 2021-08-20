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
        self.user = User.objects.create_user(username='sai')
        self.topic = Topic.objects.create(name='decorator')
        self.entry = Entry.objects.create(topic=self.topic, entry='Adding the functionality to the existing function')
        self.tag = Tags.objects.create(tag='decorators')

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
        url = reverse('pybasic:topics', kwargs={'user_id': self.user.id})
        response = self.client.get(url)
        html = response.content.decode('utf8')
        self.assertIn('<title>Topics</title>', html)
        self.assertTemplateUsed(response, 'pybasic/topics.html')

    def test_topic_detail_view(self):
        """
            Function to test the topic detail view function is rendering the correct page.
        """
        url = reverse('pybasic:topic-detail', kwargs={'user_id': self.user.id, 'topic_id': self.topic.id})
        response = self.client.get(url)
        html = response.content.decode('utf8')
        self.assertIn('<title>TopicDetail</title>', html)
        self.assertTemplateUsed(response, 'pybasic/topic_detail.html')

    def tag_view(self):
        """
            Function to test the  view function is rendering the correct page.
        """
        url = reverse('pybasic:add-tag', kwargs={'user_id': self.user.id})
        response = self.client.get(url)
        html = response.content.decode('utf8')
        self.assertIn('<title>Add Tags</title>', html)
        self.assertTemplateUsed(response, 'pybasic/tag.html')