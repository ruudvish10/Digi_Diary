from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Q

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """The homepage for Digi Diary."""
    return render(request, "digi_diaries/index.html")

@login_required
def topics(request):
    """Show all topics or filter based on search."""
    #Get the search query
    query = request.GET.get("q", "")
    topics = Topic.objects.filter(owner=request.user).order_by("-date_added")

    if query:
        #Filter topics based on query after filtering by owner
        topics = topics.filter(Q(content__icontains=query))

    #Pass the context variable to the template
    context = {"topics": topics, "query": query}
    return render(request, "digi_diaries/topics.html", context)

#Adding a Delete method for topics
@login_required
def delete_topic(request):
    """Delete selected topics from the topics page """
    if request.method == "POST":
        #Get the IDs of the selected topics from the list
        selected_topics = request.POST.getlist("selected_topics")
        if selected_topics:
            #Delete topics that match IDs and are owned by the user
            Topic.objects.filter(id__in=selected_topics, owner=request.user).delete()
        return redirect("digi_diaries:topics")
    return redirect("digi_diaries:topics")

@login_required
def sub_topics(request, sub_topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=sub_topic_id)
    #Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by("-date_added")      #The minus sign gets the reverse order
    context = {"topic": topic, "entries": entries}
    return render(request, "digi_diaries/sub_topics.html", context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != "POST":
        #No data submitted. Create a blank form.
        form = TopicForm()
    else:
        #User enters data. Process the data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect("digi_diaries:topics")
    
    #Display a blank or invalid form.
    context = {"form": form}
    return render(request, "digi_diaries/new_topic.html", context)

@login_required
def add_sub_topic(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    if request.method != "POST":
        #No data submitted. Create a blank form.
        form = EntryForm()
    else:
        #User enters data. Process the data.
        form = EntryForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic                                 #Associates an entry with a topic
            new_entry.save()
            return redirect("digi_diaries:sub_topics", sub_topic_id=topic_id)
    
    #Display a blank or invalid form.
    context = {"topic": topic, "form": form}
    return render(request, "digi_diaries/add_sub_topic.html", context)

@login_required
def edit_sub_topic(request, sub_topic_id):
    """Edit an existing entry."""
    entry = Entry.objects.get(id=sub_topic_id)
    topic = entry.topic                 #Gets the topic associated with this entry 
    if topic.owner != request.user:
        raise Http404
    
    if request.method != "POST":
        #Initial request. Get prefilled entry form with current entry.
        form = EntryForm(instance=entry)
    else:
        #POST data submitted. Create form based on existing entry.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("digi_diaries:sub_topics", sub_topic_id=topic.id)
        
    #Display a blank or invalid form.
    context = {"entry": entry, "topic": topic, "form": form}
    return render(request, "digi_diaries/edit_sub_topic.html", context)

#Adding a Delete Entry method for entries
@login_required
def delete_sub_topic(request):
    """Delete selected entries."""
    if request.method == "POST":
        #Get IDs of selected entries 
        selected_entries = request.POST.getlist("selected_entries")

        if selected_entries:
            #Retrieve the topic_id of the selected entries
            topic_id = Entry.objects.filter(id__in=selected_entries, topic__owner=request.user).values_list("topic__id", flat=True).first()
        
        if topic_id:
            #Delete selected entries
            Entry.objects.filter(id__in=selected_entries, topic__owner=request.user).delete()
            return redirect("digi_diaries:sub_topics", sub_topic_id=topic_id)
    
    #Default if no entries are selected
    return redirect("digi_diaries:topic")
        

"""def delete_entry(request, entry_id):
    #Delete an existing entry
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method == "POST":
        entry.delete()
        return redirect("digi_diaries:topic", topic_id=topic.id)
    
    context = {"entry": entry, "topic": topic}
    return render(request, "digi_diaries/delete_entry.html", context)
    """

#Adding a Edit Topic method for topics
@login_required
def edit_topic(request, topic_id):
    """Edit an existing topic"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    
    if request.method =="POST":
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("digi_diaries:topics")
    else:
        form = TopicForm(instance=topic)
    
    context = {"topic": topic, "form": form}
    return render(request, "digi_diaries/edit_topic.html", context)



