from django.views.generic import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Models
from .models import Document


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def home(request):
    return render(request, 'index.html')


@login_required
def doc_all(request):
    docs = Document.objects.all()
    return render(request, 'doc_all.html', {'docs': docs})


class DocCreate(CreateView):
    model = Document
    fields = ['name', 'url', 'description']


class DocDelete(DeleteView):
    model = Document
    success_url = '/docs/'


class DocUpdate(UpdateView):
    model = Document
    fields = ['name', 'url', 'description']


@login_required
def doc(request, doc_id):
    doc = Document.objects.get(id=doc_id)
    return render(request, 'doc.html', {'doc': doc})
