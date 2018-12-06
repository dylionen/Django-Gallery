from django.shortcuts import render
from django.contrib.auth import authenticate
from personal.forms import ContactMe
from django.shortcuts import render,get_list_or_404,redirect, get_object_or_404
from django.views.generic.edit import FormView


def index(request):
    return render(request, 'home.html')

def contactme(request):
    return render(request, 'contact.html')

def contact_new(request):
    

    if request.method == "POST":
        form = ContactMe(request.POST)
        if form.is_valid():
            
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('index')
    else:
        form = ContactMe()
    return render(request, 'comment_edit.html', {'form': form})



