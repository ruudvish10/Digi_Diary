from django import forms
from .models import Topic, Entry
from ckeditor.widgets import CKEditorWidget

class TopicForm(forms.ModelForm):
    """Class to create a form."""
    class Meta:
        model = Topic
        fields = ["content"]
        labels = {"content": ""}

class EntryForm(forms.ModelForm):
    """Class to create entries for topics."""
    class Meta:
        model = Entry
        fields = ["content"]
        labels = {"content": ""}
        content = forms.CharField(widget=CKEditorWidget())
    
    
