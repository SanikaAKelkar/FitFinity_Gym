from django.db import models

# Create your models here.
# in this file we create a database table


class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=12)
    description = models.TextField()

    def __str__(self):
        return self.email


class Trainer(models.Model):
    name = models.CharField(max_length=55)
    gender = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    salary = models.IntegerField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name


class MembershipPlan(models.Model):
    plan = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.plan} - {self.price}"


class Enrollment(models.Model):
    FullName = models.CharField(max_length=25)
    Email = models.EmailField()
    Gender = models.CharField(max_length=25)
    PhoneNumber = models.CharField(max_length=12)
    DOB = models.CharField(max_length=50)
    SelectMembershipPlan = models.CharField(max_length=50)
    SelectTrainer = models.CharField(max_length=55)
    Reference = models.CharField(max_length=55)
    Address = models.TextField()
    paymentStatus = models.CharField(max_length=55, blank=True, null=True)
    Price = models.IntegerField(null=True, default=0)
    DueDate = models.DateTimeField(blank=True, null=True)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.FullName


class Gallery(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='gallery')
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __int__(self):
        return self.id


class Attendance(models.Model):
    Selectdate = models.DateTimeField(auto_now_add=True)
    phonenumber = models.CharField(max_length=15)
    Login = models.CharField(max_length=100)
    Logout = models.CharField(max_length=100)
    SelectWorkout = models.CharField(max_length=100)
    TrainedBy = models.CharField(max_length=100)

    def __int__(self):
        return self.phonenumber
