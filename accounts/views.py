from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != "POST":
        #Create a blank registration form
        form = UserCreationForm()
    else:
        #Save user data and create new user
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #Log in new user and redirect to homepage
            login(request, new_user)
            return redirect("digi_diaries:index")

    #Blank or invalid form
    context = {"form": form}
    return render(request, "registration/register.html", context) 
