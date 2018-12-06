from django.shortcuts import render,get_list_or_404,redirect, get_object_or_404
from .forms import CommentForm
from ctypes.wintypes import CHAR

def post_new(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/drinklist/'+str(post.news.id))
    else:
        form = CommentForm()
    return render(request, 'comment_edit.html', {'form': form})