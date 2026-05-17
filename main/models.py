from django.db import models

class Student (models.Model):
    name = models.CharField (max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class teacher: 
    pass

class Student_System(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=100)
    facult = models.CharField(max_length=100)

