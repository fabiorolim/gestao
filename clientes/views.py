from django.shortcuts import render, redirect, get_object_or_404
from .models import Person
from .forms import PersonForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def ola(request):
    return render(request, 'index.html')


@login_required
def list(request):
    persons = Person.objects.all()
    return render(request, 'person_list.html', {'persons': persons})


@login_required
def new(request):
    form = PersonForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None,
                      request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def delete(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.POST:
        person.delete()
        return redirect('person_list')
    return render(request, 'confirm_delete_person.html', {'person': person})
