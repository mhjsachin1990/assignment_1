from django.db import models


class Student(models.Model):
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=255)
    dob=models.DateField()
    roll_number=models.IntegerField()
    department_name=models.CharField(max_length=255)
    course_name=models.CharField(max_length=255)
    semister_number=models.IntegerField()
    age=models.IntegerField(default=0)

    def __str__(self):
        return self.firstname


class Department(models.Model):
    department_name=models.CharField(max_length=255)
    course_number=models.IntegerField()
    teacher_number=models.IntegerField()
