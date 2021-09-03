from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Types(models.TextChoices):
        Teacher = "TEACHER", "Teacher"
        Student = "STUDENT", "Student"

    base_type = Types.Teacher

    # What type of user are we?
    type = models.CharField(
        _("Type"), max_length=50, choices=Types.choices, default=base_type
    )

    # First Name and Last Name Do Not Cover Name Patterns
    # Around the Globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class TeacherManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.Teacher)


class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.Student)

# more feilds of Teachers
class TeacherMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Subject = models.TextField()


class Teacher(User):
    base_type = User.Types.Teacher
    objects = TeacherManager()

    class Meta:
        proxy = True

    def order(self):
        return "Study"

# more feilds of Students
class StudentMore(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    clas = models.CharField(max_length=255)


class Student(User):
    base_type = User.Types.Student
    objects = StudentManager()

    @property
    def more(self):
        return self.studentmore

    class Meta:
        proxy = True

    def obey(self):
        return "Ok Teacher"
