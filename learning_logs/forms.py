from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Class to create a form."""
    class Meta:
        model = Topic
        fields = ["text"]
        labels = {"text": ""}

class EntryForm(forms.ModelForm):
    """Class to create entries for topics."""
    class Meta:
        model = Entry
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={"cols": 80})}
    
    
