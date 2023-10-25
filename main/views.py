from django.shortcuts import render, redirect
from .models import *


def index_view(request):
    context = {
        'tasks': Todo.objects.all()

    }
    return render(request,'index.html', context)



def create_tack_view(request):
    if request.method == "POST":
        tack = request.POST['task']
        Todo.objects.create(
            tack=tack
        )
    return redirect("index_url")



def swap_status_deleted(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.status = 'DELETED'
    todo.save()
    return redirect('index_url')


def swap_status_finished(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.status = 'FINISHED'
    todo.save()
    return redirect('index_url')

def inprogress_view(request):
    context = {
        'tacks': Todo.objects.filter(status="In Progress")

    }
    return render(request,'inprogress.html', context)


def delete_task_view(request, pk):
    task = Todo.objects.get(pk=pk)
    task.delete()
    return redirect('index_url')

def finished_view(request):
    context={
        'tack':Todo.objects.filter(status="FINISHED")
    }
    return render(request,'finished.html', context)



def deleted_task_view(request):
    context={
        'tacks':Todo.objects.filter(status="DELETED")
    }
    return render(request,'deleted.html', context)