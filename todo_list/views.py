from django.shortcuts import render, redirect
from django.contrib import messages
from django.forms import modelform_factory
# from django.core.files.storage import FileSystemStorage
from .models import List
from .forms import ListForm

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item saved successfully.')
        else:
            messages.error(request, f'Item not saved properly: {form.errors.as_data()}')
        return redirect('home')
        # return HttpResponseRedirect(reverse("some_app.views.index"))

    todo_list = List.objects.all()
    return render(request, 'todo_list/home.html', { 'todo_list': todo_list })

def get_item(item_id):
    try:
        item = List.objects.get(pk=item_id)
    except List.DoesNotExist:
        item = None

    return item

def uncross(request, item_id):
    item = get_item(item_id)
    if item:
        item.completed = False
        item.save()
    else:
       messages.error(request, "The item doesn't exist!")

    return redirect('home')

def cross_off(request, item_id):
    item = get_item(item_id)
    if item:
        item.completed = True
        item.save()
    else:
       messages.error(request, "The item doesn't exist!")

    return redirect('home')

def edit(request, item_id):
    if request.method == 'POST':
        item = List.objects.get(pk=item_id)
        form = ListForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item saved successfully.')
        else:
            messages.error(request, f'Item not saved properly: {form.errors.as_data()}')
        return redirect('home')
    else:
        item = get_item(item_id)
        if item:
            return render(request, 'todo_list/edit.html', { 'item': item })
        else:
            messages.error(request, "The item doesn't exist!")
            return redirect('home')

def delete(request, item_id):
    item = get_item(item_id)
    if item:
        item.delete()
        messages.success(request, "Item deleted.")
    else:
        messages.error(request, "The item doesn't exist!")
    return redirect('home')

def upload(request, item_id):
    if request.method == 'POST':
        if not 'document' in request.FILES:
            messages.success(request, 'No file uploaded.')
        else:
            item = List.objects.get(pk=item_id)
            ListForm_ = modelform_factory(List, fields=("document",))
            form = ListForm_(request.POST, request.FILES, instance=item)
            if form.is_valid():
                form.save()
                messages.success(request, 'File saved successfully.')
            else:
                messages.error(request, f'File not saved properly: {form.errors.as_data()}')
        return redirect('home')
    else:
        item = get_item(item_id)
        if item:
            return render(request, 'todo_list/upload.html', { 'item': item })
        else:
            messages.error(request, "The item doesn't exist!")
            return redirect('home')
