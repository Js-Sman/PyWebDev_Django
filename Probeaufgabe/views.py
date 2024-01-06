from django.shortcuts import render, redirect

from Probeaufgabe.forms import ProbeaufgabeForm
from Probeaufgabe.models import Students


# Create your views here.
def probe_view_funktion(request):
    students = Students.objects.all()

    context = {"students": students}

    return render(request, 'probeTemplates/probeMainTemplate.html', context)


def new_student(request):
    if request.method == 'POST':
        form = ProbeaufgabeForm(request.POST)
        if form.is_valid():
            student = Students()

            student.name = form.cleaned_data['name']
            student.semester = form.cleaned_data['semester']
            student.start_date = form.cleaned_data['start_date']
            student.average = form.cleaned_data['average']

            student.save()

            return redirect("probe_view_funktion")

    context = {"form": ProbeaufgabeForm()}
    return render(request, "probeTemplates/edit.html", context)
