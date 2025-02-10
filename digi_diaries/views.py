from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.db.models import Q

from .models import Topic, Subtopic, Entry
from .forms import TopicForm, SubtopicForm, EntryForm

def index(request):
    """The homepage for Digi Diary."""
    return render(request, "digi_diaries/index.html")

#Method for topics
@login_required
def topics(request):
    """Show all topics or filter based on search."""
    #Get the search query
    query = request.GET.get("q", "")
    topics = Topic.objects.filter(owner=request.user).order_by("title")

    if query:
        #Filter topics based on query after filtering by owner
        topics = topics.filter(Q(content__icontains=query))

    #Pass the context variable to the template
    context = {"topics": topics, "query": query}
    return render(request, "digi_diaries/topics.html", context)

#Method for adding new topics
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

#Method for editing topics
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
        form.fields["title"].widget.attrs["placeholder"] = "Edit topic here..."
    
    context = {"topic": topic, "form": form}
    return render(request, "digi_diaries/edit_topic.html", context)

#Method for deleting topics
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

#Method for sub topics
@login_required
def sub_topics(request, topic_id):
    """Show a single sub topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    #Make sure the topic belongs to the current user.
    if topic.owner != request.user:
        raise Http404
    #Search query
    query = request.GET.get("q", "")
    #Filter for sub topic using the related name
    sub_topic = topic.subtopics.filter(Q(content__icontains=query)).order_by("title")  
    #Used the related_name value from the db for sorting
    #sub_topic = topic.subtopics.order_by("-date_added")           
    
    context = {"topic": topic,"sub_topic": sub_topic, "query": query}
    return render(request, "digi_diaries/sub_topics.html", context)

#Method to add sub topic
@login_required
def add_sub_topic(request, topic_id):
    """Add a new sub topic for a particular topic."""
    topic = Topic.objects.get(id=topic_id, owner=request.user)

    if request.method != "POST":
        #No data submitted. Create a blank form.
        form = SubtopicForm()
    else:
        #User enters data. Process the data.
        form = SubtopicForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            sub_topic = form.save(commit=False)
            sub_topic.topic = topic                                 #Associates an esub topic with a topic
            sub_topic.save()
            return redirect("digi_diaries:sub_topics", topic_id=topic_id)
    
    #Display a blank or invalid form.
    context = {"topic": topic, "form": form}
    return render(request, "digi_diaries/add_sub_topic.html", context)

#Method for editing sub topics
@login_required
def edit_sub_topic(request, sub_topic_id):
    """Edit an existing entry."""
    sub_topic = Subtopic.objects.get(id=sub_topic_id)
    #Gets the topic associated with this sub topic
    topic = sub_topic.topic                  
    if topic.owner != request.user:
        raise Http404
    
    if request.method != "POST":
        #Initial request. Get prefilled entry form with current entry.
        form = SubtopicForm(instance=sub_topic)
        form.fields["title"].widget.attrs["placeholder"] = "Edit sub-topic here..."
    else:
        #POST data submitted. Create form based on existing entry.
        form = SubtopicForm(instance=sub_topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("digi_diaries:sub_topics", topic_id=topic.id)
        
    #Display a blank or invalid form.
    context = {"sub_topic": sub_topic, "topic": topic, "form": form}
    return render(request, "digi_diaries/edit_sub_topic.html", context)

#Method for deleting sub topics
@login_required
def delete_sub_topic(request):
    """Delete selected sub topics."""
    if request.method == "POST":
        #Get IDs of selected entries 
        selected_subtopics = request.POST.getlist("selected_subtopics")

        if selected_subtopics:
            #Retrieve the topic_id of the selected entries
            topic_id = Subtopic.objects.filter(id__in=selected_subtopics, topic__owner=request.user).values_list("topic__id", flat=True).first()
        
        if topic_id:
            #Delete selected entries
            Subtopic.objects.filter(id__in=selected_subtopics, topic__owner=request.user).delete()
            return redirect("digi_diaries:sub_topics", topic_id=topic_id)
    
    #Default if no entries are selected
    return redirect("digi_diaries:topic")

#Entries for sub topics
def sub_topic_entries(request, topic_id, sub_topic_id):
    """Show sub topics and their entries."""
    topic = Topic.objects.get(id=topic_id)
    sub_topic = Subtopic.objects.get(id=sub_topic_id, topic__owner=request.user)
    #Filter for search using the related name
    query = request.GET.get("q", "")
    entries = sub_topic.entries.filter(Q(title__icontains=query)).order_by("title")
    #entries = sub_topic.entries.order_by("-date_added")
    context = {"topic": topic, "sub_topic": sub_topic, "entries": entries, "query": query}
    return render(request, "digi_diaries/entries.html", context )

#Edit entries
@login_required
def edit_entries(request, sub_topic_id, entry_id):
    """Edit an entry."""
    sub_topic = Subtopic.objects.get(id=sub_topic_id)
    topic = sub_topic.topic
    entry = Entry.objects.get(id=entry_id)
    if entry.sub_topic.topic.owner != request.user:
        raise Http404
    
    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        #POST data is submitted
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("digi_diaries:sub_topic_entries", topic_id=topic.id , sub_topic_id=sub_topic_id)

    #Display a blank or invalid form.
    context = {"sub_topic": sub_topic, "entry": entry, "form": form, "topic": topic}
    return render(request, "digi_diaries/edit_entry.html", context)

#Add entries
@login_required
def add_entries(request, sub_topic_id):
    """Add an entry."""
    sub_topic = Subtopic.objects.get(id=sub_topic_id)
    topic = sub_topic.topic

    if request.method == "POST":
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.sub_topic = sub_topic
            entry.save()
            return redirect("digi_diaries:sub_topic_entries", topic.id, sub_topic.id)
    
    else:
        form = EntryForm()
       
    context = {"form": form, "topic": topic, "sub_topic": sub_topic}
    return render(request, "digi_diaries/add_entry.html", context)


#Delete entries
@login_required
def delete_entries(request):
    """Delete an entry."""
    if request.method == "POST":
        #Get IDs of selected entries 
        selected_entries = request.POST.getlist("selected_entries")

        if selected_entries:
            #Retrieve the topic and sub_topic_id of the selected entries
            entry_info = Entry.objects.filter(id__in=selected_entries, sub_topic__topic__owner=request.user).values_list("sub_topic_id", "sub_topic__topic_id").first()
        
            if entry_info:
                sub_topic_id, topic_id = entry_info

                #Delete selected entries
                Entry.objects.filter(id__in=selected_entries, sub_topic__topic__owner=request.user).delete()
                return redirect("digi_diaries:sub_topic_entries", topic_id=topic_id,sub_topic_id=sub_topic_id)
    
    #Default if no entries are selected
    return redirect("digi_diaries:sub_topics")








