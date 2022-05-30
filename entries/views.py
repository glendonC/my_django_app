from django.shortcuts import render
from .models import Entry

# Create your views here.
def index(request):
    entries = Entry.objects.order_by('-date')

    context = {'entries': entries}
    return render(request, 'entries/index.html', context)

def add(request):
    return render(request, 'entries/add.html')