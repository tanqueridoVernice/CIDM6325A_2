from django.db import models

# Create your models here.

class College(models.Model):
    name = models.CharField(max_length=100, help_text="College name")

    def __str__(self):
        return self.name
class Department(models.Model):
    name = models.CharField(max_length=100, help_text="Department name")
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Semester(models.Model):
    sem = models.CharField(max_length=50,help_text="Spring,Fall,Summer I, Summer II")

    def __str__(self):
        return self.sem
class Coursetype(models.Model):
    Coreornot = (
        ('Core','Core'),
        ('Major','Major'),
    )
    type = models.CharField(max_length=20,choices=Coreornot, default = 0)
    Core_category = models.CharField(max_length=10,help_text="010,020, ...")
    Component_area = models.CharField(max_length=50, help_text="Mathematics, Major, ...")
    def __str__(self):
        return self.Component_area
class Course(models.Model):
    c_ID = models.CharField(max_length=20, help_text="ex. CIDM 6325")
    c_name = models.CharField(max_length= 150, help_text="e-commerce and web development")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    type = models.ForeignKey(Coursetype,default = 0 ,on_delete=models.CASCADE)
    hours = models.IntegerField(default=3,help_text="number of credit hours")

    def __str__(self):
        return self.c_name

class Degree(models.Model):
    name = models.CharField(max_length=150, help_text="Degree Name")
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Degreecheck(models.Model):
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    courses = models.ManyToManyField(Course)
    def __str__(self):
        return self.degree
class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    studentID = models.CharField(max_length=15)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    coursestaken = models.ManyToManyField(Course)

    def __str__(self):
        return self.fname + ' ' + self.lname








