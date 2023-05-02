from django.shortcuts import render, redirect
from .models import TodoList

# Create your views here.
def Index(request):
    context = {}
    if request.method == "POST":
        new_task = request.POST.get('new-task')
        add_task = TodoList(dec=new_task)
        add_task.save()
        return redirect('Index')
    
    
    Totos = TodoList.objects.all()
    context['Totos'] = Totos
    
    return render(request, 'index.html', context)