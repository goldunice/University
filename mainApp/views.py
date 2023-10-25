from django.shortcuts import render, redirect
from .models import *
from .forms import *


def homepage(request):
    return render(request, 'homepage.html')


def majors(request):
    if request.method == 'POST':
        form = MajorForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/majors/")
    word = request.GET.get("search")
    result = Major.objects.all()
    if word:
        result = result.filter(name__contains=word)
    content = {
        "majors": result,
        "major_form": MajorForm()
    }
    return render(request, 'majors.html', content)


def delete_major(request, num):
    Major.objects.get(id=num).delete()
    return redirect("/majors/")


def update_major(request, num):
    if request.method == 'POST':
        Major.objects.filter(id=num).update(
            name=request.POST.get("name"),
            active=request.POST.get("active")
        )
        return redirect("/majors/")
    content = {
        "majors": Major.objects.get(id=num)
    }
    return render(request, 'update_major.html', content)


def subjects(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/subjects/")

    word = request.GET.get("search")
    result = Subject.objects.all()
    if word:
        result = result.filter(name__contains=word)
    content = {
        "subjects": result,
        "subject_form": SubjectForm()
    }
    return render(request, 'subjects.html', content)


def delete_subject(request, num):
    Subject.objects.get(id=num).delete()
    return redirect("/subjects/")


def update_subject(request, num):
    if request.method == 'POST':
        Subject.objects.filter(id=num).update(
            name=request.POST.get("name"),
            major=Major.objects.get(id=request.POST.get("major")),
            main=request.POST.get("main")
        )
        return redirect("/subjects/")
    content = {
        "subjects": Subject.objects.get(id=num),
        "majors": Major.objects.all()
    }
    return render(request, 'update_subject.html', content)


def teachers(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/teachers/")
    word = request.GET.get("search")
    result = Teacher.objects.all()
    if word:
        result = result.filter(name__contains=word)
    content = {
        "teacher_form": TeacherForm(),
        "teachers": result
    }
    return render(request, 'teachers.html', content)


def delete_teacher(request, num):
    Teacher.objects.get(id=num).delete()
    return redirect("/teachers/")


Gender = [g[0] for g in gender]


def update_teacher(request, num):
    if request.method == 'POST':
        Teacher.objects.filter(id=num).update(
            name=request.POST.get("name"),
            gender=request.POST.get("gender"),
            age=request.POST.get("age"),
            level=request.POST.get("level"),
            subject=Subject.objects.get(id=request.POST.get("subject"))
        )
        return redirect("/teachers/")
    content = {
        "subjects": Subject.objects.all(),
        "genders": Gender,
        "teachers": Teacher.objects.get(id=num)
    }
    return render(request, 'update_teacher.html', content)
