from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.http import require_POST

from forms.models import Entry
from forms.forms import EntryForm

# Create your views here.
def entry(request):

    form = EntryForm(request.POST or None)
    context = {'form': form,}

    return render(request, 'forms/entry.html', context)


def confirm(request):
    form = EntryForm(request.POST)
    context = {'form': form,}

    if form.is_valid():
        return render(request, 'forms/confirm.html', context)

    return render(request, 'forms/entry.html', context)


def complete(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('forms:complete')
    else:
        form = EntryForm()
    
    return render(request, 'forms/complete.html', {'form': form})