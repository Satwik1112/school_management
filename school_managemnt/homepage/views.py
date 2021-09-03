from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import User, Teacher, Student
from .serializers import Register_Serializer


# Create your views here.


# use for display homepage
def homepage(request):
    return render(request, 'homepage.html')


def register_view(GenericAPIView):
    def post(self, request):
        user = request.data
        serializer = Register_Serializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        return Response(user_data, status=status.HTTP_201_CREATED)


# use for teacher signup
def signup_teacher(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        subject = request.POST['subject']
        fl = name.split(' ')
        first_name = fl[0]
        last_name = fl[1]
        u = User.objects.create_user(username=username, email=email, password=password, is_staff=True, first_name=first_name,
                                     last_name=last_name)# is staff is True for teacher also for true for superuser
        t = Teacher.objects.all()
        print(t)
        u.save()
        print('User is created for u', u)
        return redirect('/')
    else:
        return render(request, 'signupTeacher.html')


# use for student signup
def signup_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        name = request.POST['name']
        password = request.POST['password']
        clas = request.POST['class']
        fl = name.split(' ')
        first_name = fl[0]
        last_name = fl[1]
        u = User.objects.create_user(username=username, email=email, password=password, is_staff=False, first_name=first_name,
                                     last_name=last_name, type='STUDENT')# is staff if false for student
        u.save()
        print('User is created for u', u)
        s = Student.objects.all()
        print(s)
        return redirect('/')
    else:
        return render(request, 'signupStudent.html')


# use for login
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        error_email = False
        error_password = False
        if email is None:
            error_email = True
        if password is None:
            error_password = True
        if error_email and error_password:
            return render(request, 'login.html', {'error': 'Email or Password is blank'})

        return redirect('/')

    else:
        return render(request, 'login.html')
