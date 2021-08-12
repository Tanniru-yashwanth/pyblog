from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """
    class to create topic table in database
    """
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        method to display the topic name instead of object
        """
        return f"{self.name}"


class Entry(models.Model):
    """
    class to create entry table in database
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    entry = models.TextField()
    created = models.DateTimeField(auto_now_add=models.CASCADE)

    def __str__(self):
        """
        method to display the topic name instead of object
        """
        return f"{self.entry}"

    class Meta:
        """
        This is used to store the name of Entries instead of Entrys
        """
        verbose_name_plural = 'Entries'


class Comment(models.Model):
    """
    class to create comment table in database
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        method to display the topic name instead of object
        """
        return f"{self.comment}"


class Questions(models.Model):
    """
    class to question table in database
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        method to display the topic name instead of object
        """
        return f"{self.question}"
