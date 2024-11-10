from django.shortcuts import render, redirect
from .models import Title, Choice

# Create your views here.

def home(request):
    titles = Title.objects.all()
    return render(request, 'home.html', {'titles': titles})

def votedetails(request, id):
    title = Title.objects.get(id=id)
    choices = title.choice.all()
    context = {'title': title, 'choices': choices}
   
    return render(request, 'title.html', context)

def vote(request, id):
    title = Title.objects.get(id=id)
    choices = title.choice.all()
    context = {'title': title, 'choices': choices}    
    return render (request, 'vote.html', context)


def voted(request):
    if request.method == 'POST':
        selected = request.POST.get('sel')
        selected = selected[:-1]
        print(selected)
        choice = Choice.objects.get(id=selected)
        choice.votes += 1
        choice.save()
        id = choice.title.id
        return redirect(votedetails, id)
    return render(request, 'home')
