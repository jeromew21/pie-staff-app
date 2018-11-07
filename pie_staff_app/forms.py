from django.forms import ModelForm
from .models import Snippet, Issue

class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ["name", "content"]

class IssueForm(ModelForm):
    class Meta:
        model = Issue
        fields = ["name", "content"]