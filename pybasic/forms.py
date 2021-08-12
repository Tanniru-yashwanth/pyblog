from django import forms
from .models import Comment, Questions


class CommentFormDisplay(forms.ModelForm):
    """
    Class for Comment form
    """
    class Meta:
        model = Comment
        label = {"comment": ''}
        fields = ["comment"]


class QuestionForm(forms.ModelForm):
    """
    class for question form
    """
    class Meta:
        model = Questions
        label = {'ask': ''}
        fields = ['question']
