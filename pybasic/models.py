from django.db import models
from django.contrib.auth.models import User


class Tags(models.Model):
    """
    Class to provide tags to find topics easily.
    """

    tag = models.CharField(max_length=100)

    def __str__(self):
        """
        To display the name of the tags created.
        """
        return f"{self.tag}"

    class Meta:
        verbose_name_plural = "Tags"


class Topic(models.Model):
    """
    Class to create topic model with related fields to handle topics.
    """

    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tags, through='TagTopics')

    def __str__(self):
        """
        Method to display the topic name instead of object.
        """
        return f"{self.name}"


class Entry(models.Model):
    """
    Class to create entry model with related fields linked to topic.
    """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    entry = models.TextField()
    created = models.DateTimeField(auto_now_add=models.CASCADE)

    def __str__(self):
        """
        Method to display the topic name instead of object.
        """
        return f"{self.entry}"

    class Meta:
        """
        This is used to store the name of Entries instead of Entrys.
        """

        verbose_name_plural = "Entries"


class Comment(models.Model):
    """
    Class to create comment model to provide comment feature to the users.
    """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Method to display the topic name instead of object.
        """
        return f"{self.comment}"


class Questions(models.Model):
    """
    Class to create questions model to provide the
    facility of clarifying doubts about the topic for the user.
    """

    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Method to display the topic name instead of object.
        """
        return f"{self.question}"


class TagTopics(models.Model):
    """
    Class for creating custom through model.
    """
    tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    tag_added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tag}-{self.topic}"
