from django.shortcuts import render, redirect
from . forms import WidgetForm
from . models import Widget
# Create your views here.

def home(request):
    widget_list = Widget.objects.all()
    if request.method == 'POST':
        form = WidgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = WidgetForm()
        return render(request, 'home.html', {'form': form, 'widget_list': widget_list})

def delete(request, wid_id):
    widget = Widget.objects.get(id=wid_id)
    widget.delete()
    return redirect('home')