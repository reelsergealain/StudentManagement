from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Sum
from student.forms import AddStudentForm
from .models import Student

def index(request):
    students = Student.objects.all().order_by('-created_at')
    sold_count = students.filter(sold=True).count()
    not_sold_count = students.filter(sold=False).count()
    total_photos = students.aggregate(Sum('num_of_pic'))['num_of_pic__sum'] or 0
    
    context = {
        'students': students,
        'sold_count': sold_count,
        'not_sold_count': not_sold_count,
        'total_photos': total_photos,
    }
    return render(request, 'student/index.html', context)

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    parrain = student.parrain  # Récupérer le parrain de l'étudiant
    return render(request, 'student/student_detail.html', {'student': student, 'parrain': parrain})

def add_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            # Get form data
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone = form.cleaned_data['phone']
            code_parain = form.cleaned_data['code_parain']

            # Check if referral code is valid and unique
            if code_parain and Student.objects.filter(code_parainage=code_parain).exists():
                parrain = Student.objects.get(code_parainage=code_parain)
                parrain.num_of_pic += 1  # Increase the parrain's photo count by 1
                parrain.save()

            # Create a new student
            new_student = Student(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
            )
            new_student.save()
            return redirect('index')

    else:
        form = AddStudentForm()

    context = {'form': form}
    return render(request, 'student/add_student.html', context)
