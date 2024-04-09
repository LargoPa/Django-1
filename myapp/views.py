from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
    title = 'Django Course!!'
    return render(request, 'index.html',{
        'title': title
    })

def hello(request, username):
    return HttpResponse(f'<h1>Hello {username}</h1>')

def about(request):
    return HttpResponse('<h2>About</h2>')

def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def tasks(request, id):
    task = get_object_or_404(Task, id=id)
    return HttpResponse(f'task: {task.title}')
