from django.shortcuts import render

from django.shortcuts import render,redirect
from .models import TodoList, Group
from users.models import CustomUser
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user = request.user
    todos = TodoList.objects.filter(user=user)
    groups = Group.objects.all()
    if request.method == "POST":
        if "add_task" in request.POST:
            title = request.POST["title"]
            description = request.POST.get('description', "")
            group = request.POST["group_select"]
            if group == '':
                group = 'General'
            Todo = TodoList(title=title, description=description, group=Group.objects.get(name=group), user=user)
            Todo.save()
            return redirect("/")

        if "delete_task" in request.POST:
            print(request.POST)
            try:
                checkedlist = request.POST.getlist('checkedbox')
            except:
                return

            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()
    return render(request, "todo/index.html", {"todos": todos, "groups": groups})

@login_required
def toggle_done_undone(request):

    classes = request.GET.get('classes', None)
    toggle_val = classes.split()[1]

    todo_id = request.GET.get('todo_id', None)
    todo_id = todo_id.split('_')[1]

    todo = TodoList.objects.get(id=int(todo_id))
    if toggle_val == 'mark_done':
        todo.status = 'd'
        todo.save()
        status = 'd'
    else:
        todo.status = 'p'
        todo.save()
        status = 'p'
    data = {
       'status': status
    }
    return JsonResponse(data)



@login_required
def by_group(request, group):
    user = request.user
    todos = TodoList.objects.filter(user=user, group=Group.objects.get(name=group))
    groups = Group.objects.all()
    if request.method == "POST":
        if "add_task" in request.POST:
            title = request.POST["title"]
            description = request.POST.get('description', "")
            get_group = request.POST["group_select"]
            if get_group == '':
                get_group = 'General'
            Todo = TodoList(title=title, description=description, group=Group.objects.get(name=get_group), user=user)
            Todo.save()
            return redirect(f"/{group}")

        if "delete_task" in request.POST:
            print(request.POST)
            try:
                checkedlist = request.POST.getlist('checkedbox')
            except:
                return

            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()
    return render(request, "todo/index.html", {"todos": todos, "groups": groups})

