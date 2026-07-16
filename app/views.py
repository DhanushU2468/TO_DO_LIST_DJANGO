from django.shortcuts import redirect, render

from .models import *


def home(request):
    data=Task.objects.all()
    return render (request,'home.html',{'data':data})

def add(request):
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['description']
        Task.objects.create(
            title=title,
            desc=desc,
    )
    return render(request,'add.html')
def update(request,pk):
    data=Task.objects.get(id=pk)
    if request.method=='POST':
        title=request.POST['title']
        desc=request.POST['description']
        data.title=title
        data.desc=desc
        data.save()
        return redirect('home')
        
    return render(request,'update.html',{'data':data})
def completed(request,pk):
    data=Task.objects.get(id=pk)
    CompleteTask.objects.create(
        title=data.title,
        desc=data.desc
    )
    data.delete()
    return redirect('complete')

def trash(request):
    trash_data=Trash.objects.all()
    return render(request,'trash.html',{'trash_data':trash_data})

def hdelete(request,pk):
    data=Task.objects.get(id=pk)
    Trash.objects.create(
        title=data.title,
        desc=data.desc
    )
    data.delete()
    return redirect('trash')

def about(request):
    return render(request,'about.html')

def complete(request):
    comp_data=CompleteTask.objects.all()
    return render(request,'completed.html',{'comp_data':comp_data})
# Create your views here.
