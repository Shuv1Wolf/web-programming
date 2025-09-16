from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm
from django.http import Http404


@login_required
def task_list(request):
    """Список задач пользователя."""
    tasks = Task.objects.filter(owner=request.user).order_by('-date_created')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_detail(request, task_id):
    """Просмотр детали задачи."""
    task = get_object_or_404(Task, id=task_id)
    if task.owner != request.user:
        raise Http404
    return render(request, 'tasks/task_detail.html', {'task': task})

@login_required
def new_task(request):
    """Создание новой задачи."""
    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.owner = request.user
            task.save()
            return redirect('tasks:task_list')
    return render(request, 'tasks/task_form.html', {'form': form})

@login_required
def edit_task(request, task_id):
    """Редактирование существующей задачи."""
    task = get_object_or_404(Task, id=task_id)
    if task.owner != request.user:
        raise Http404
    if request.method != 'POST':
        form = TaskForm(instance=task)
    else:
        form = TaskForm(instance=task, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('tasks:task_list')
    return render(request, 'tasks/task_form.html', {'form': form, 'task': task})

@login_required
def delete_task(request, task_id):
    """Удаление задачи."""
    task = get_object_or_404(Task, id=task_id)
    if task.owner != request.user:
        raise Http404
    if request.method == 'POST':
        task.delete()
        return redirect('tasks:task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task': task})
