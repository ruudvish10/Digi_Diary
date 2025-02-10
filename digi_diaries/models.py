from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

#Model for topics
class Topic(models.Model):
    """A topic the user has in mind."""
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    title = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.title
    
#Model for subtopics
class Subtopic(models.Model):
    """A subtopic related to a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="subtopics")
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField()
    title = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the subtopic."""
        return self.title

#Model for entries
class Entry(models.Model):
    """ Thoughts/ideas about a specific topic."""
    sub_topic = models.ForeignKey(Subtopic, on_delete=models.CASCADE, related_name="entries")
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField()
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a string representation of the entry."""
        return self.title

    