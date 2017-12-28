from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse

from forms.models import Entry
from forms.forms import EntryForm

# Create your views here.
#def index(request):
def entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.save()
            return redirect('forms:complete')
    else:
        form = EntryForm()
    
    return render(request, 'forms/entry.html', {'form': form})


def complete(request):

    return render(request, 'forms/complete.html')