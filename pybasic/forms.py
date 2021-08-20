from django import forms
from .models import Comment, Questions, Tags, TagTopics


class CommentFormDisplay(forms.ModelForm):
    """
    Class to create comment form to give the facility of commenting about the topic.

    """

    class Meta:
        model = Comment
        label = {"comment": "comment"}
        fields = ["comment", 'profession', 'json_field']


class QuestionForm(forms.ModelForm):
    """
    class to create question form to give the facility of asking questions about the topic.
    """

    class Meta:
        model = Questions
        label = {"question": "question"}
        fields = ["question", 'profession', 'json_field']


class TagForm(forms.ModelForm):
    """
    Class to create tag form to provide the facility of adding tags and removing.
    """

    class Meta:
        model = Tags
        label = {"tag": "tags"}
        fields = ['tag']


class TagsTopicsForm(forms.ModelForm):
    """
    Class to create tags_topics form to provide the facility of adding tags to the topic.
    """
    class Meta:
        model = TagTopics
        fields = ['tag']