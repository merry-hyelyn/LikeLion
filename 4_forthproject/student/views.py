from django.shortcuts import render, get_object_or_404
from .models import Student
# Create your views here.


def index(request):
    student = Student.objects.all
    return render(request, 'index.html', {
        "students": student
    })


def create_page(request):
    return render(request, 'create_page.html')


def create(request):
    student = Student()

    student.name = request.GET["name"]
    student.department = request.GET["department"]
    student.admission_year = request.GET["admission_year"]
    student.student_number = request.GET["student_number"]
    student.level = request.GET["level"]
    student.grade_avg = request.GET["grade_avg"]

    student.save()

    return redirect("index")


def read(request, id):
    student = get_object_or_404(Student, pk=id)

    return render(reauest, 'read.html', {
        "student": student,
    })


def update(request):
    student = Student()

    student.name = request.GET["name"]
    student.department = request.GET["department"]
    student.admission_year = request.GET["admission_year"]
    student.student_number = request.GET["student_number"]
    student.level = request.GET["level"]
    student.grade_avg = request.GET["grade_avg"]

    student.save()

    return redirect("index")


def update_page(request, id):
    student = get_object_or_404(Student, pk=id)

    return render(request, 'update_page.html', {
        "student": student,
    })


def delete(request, id):
    student = get_object_or_404(Student, pk=id)
    student.delete()

    return redirect("index")
