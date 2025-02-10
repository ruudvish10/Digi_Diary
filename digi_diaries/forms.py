from django import forms
from .models import Topic, Subtopic, Entry
from ckeditor.widgets import CKEditorWidget

#Form for topics
class TopicForm(forms.ModelForm):
    """Class to create a form."""
    class Meta:
        model = Topic
        fields = ["title"]
        labels = {"title": ""}
        widgets = {"title": forms.TextInput(attrs={"placeholder": "Enter a topic here..","class": "form-control", "maxlength": 255, "style": "background-color:rgb(222, 224, 228); color:rgb(10, 9, 9); border: 2px solid #495057;"})}

#Form for sub topics
class SubtopicForm(forms.ModelForm):
    """Class to create sub topics."""
    class Meta:
        model = Subtopic
        fields = ["title"]
        labels = {"title": ""}
        widgets = {"title": forms.TextInput(attrs={"placeholder": "Enter a sub-topic here..","class": "form-control", "maxlength": 255, "style": "background-color:rgb(222, 224, 228); color:rgb(10, 9, 9); border: 2px solid #495057;"})}
        #content = forms.CharField(widget=CKEditorWidget())

#Form for entries
class EntryForm(forms.ModelForm):
    """Class to create entries for topics."""
    class Meta:
        model = Entry
        fields = ["title", "content"]
        labels = {"title": "", "content": ""}
        content = forms.CharField(widget=CKEditorWidget())
        widgets = {"title": forms.TextInput(attrs={"placeholder": "Enter a title here..", "style": "background-color:rgb(222, 224, 228); color:rgb(10, 9, 9); border: 2px solid #495057;"})}
    
    
