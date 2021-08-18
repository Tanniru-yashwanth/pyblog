from django import forms
from .models import Comment, Questions


class CommentFormDisplay(forms.ModelForm):
    """
    Class to create comment form to give the facility of commenting about the topic.

    """

    class Meta:
        model = Comment
        label = {"comment": ""}
        fields = ["comment", 'profession', 'json_field']


class QuestionForm(forms.ModelForm):
    """
    class to create question form to give the facility of asking questions about the topic.
    """

    class Meta:
        model = Questions
        label = {"ask": ""}
        fields = ["question", 'profession', 'json_field']
