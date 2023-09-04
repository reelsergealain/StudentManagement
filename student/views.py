from django.shortcuts import redirect, render

from student.forms import AddStudentForm
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'student/index.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            # Get form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            code_parainage = form.cleaned_data['code_parainage']

            # Check if referral code is valid (using Student.is_valid_referral_code)
            if code_parainage:
                if not Student.is_valid_referral_code(code_parainage):
                    form.add_error('code_parainage', 'Invalid referral code')
                    return render(request, 'inscription.html', {'form': form})

            # Create a new student
            new_student = Student(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                code_parainage=code_parainage
            )
            new_student.save()

            return redirect('index')

    else:
        form = AddStudentForm()

    context = {'form': form}
    return render(request, 'student/add_student.html', context)