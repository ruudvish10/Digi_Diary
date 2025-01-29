from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Topic(models.Model):
    """A topic the user has in mind."""
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextUploadingField()

    def __str__(self):
        """Return a string representation of the model."""
        return self.content

class Entry(models.Model):
    """ Thoughts/ideas about a specific topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    content = RichTextUploadingField()

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Return a string representation of the entry."""
        return f"{self.content[:50]}..."

    