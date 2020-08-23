from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import StudentForm


def home(request):
    return render(request, 'html/main.html')


def create(request):
    form = StudentForm()

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'html/student_form.html', context)


def updateStudent(request, pk):

    student = Student.objects.get(id=pk)
    form = StudentForm(instance=student)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('/list')

    context = {'form': form}
    return render(request, 'html/student_form.html', context)




def list(request):
    students = Student.objects.all()

    context = {'students': students}
    return render(request, 'html/list.html', context)



def delete_student(request, pk):
    student = Student.objects.get(id=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('/list')

    context = {'student':student}
    return render(request, 'html/delete.html', context)