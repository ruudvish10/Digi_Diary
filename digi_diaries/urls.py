"""Defines URL patterns for digi_diaries"""

from django.urls import path

from . import views

app_name = "digi_diaries"
urlpatterns = [
    #Home page
    path("", views.index, name="index"),
    #Page that shows all topics
    path("topics/", views.topics, name="topics"),
    #Page for all sub topics
    path("sub_topics/<int:topic_id>/", views.sub_topics, name="sub_topics"),
    #Page for adding a new topic
    path("new_topic/", views.new_topic, name="new_topic"),
    #Page for editing a topic
    path("edit_topic/<int:topic_id>/", views.edit_topic, name="edit_topic"),
    #Page for adding a new sub topic
    path("add_sub_topic/<int:topic_id>/", views.add_sub_topic, name="add_sub_topic"),
    #Page for editing a sub topic
    path("edit_sub_topic/<int:sub_topic_id>/", views.edit_sub_topic, name="edit_sub_topic"),
    #Page for deleting a topic
    path("delete_topics/", views.delete_topic, name="delete_topic"),
    #Page for deleting a sub topic
    path("delete_sub_topic/", views.delete_sub_topic, name="delete_sub_topic"),
    #Page for sub topic entries
    path("sub_topic_entries/<int:topic_id>/<int:sub_topic_id>", views.sub_topic_entries, name="sub_topic_entries"),
    #Path for editing entries
    path("edit_entries/<int:sub_topic_id>/<int:entry_id>/", views.edit_entries, name="edit_entries"),
    #Path for adding entries
    path("add_entries/<int:sub_topic_id>/", views.add_entries, name="add_entries"),
    #Path for deleting entries
    path("delete_entries/", views.delete_entries, name="delete_entries"),
  

]


