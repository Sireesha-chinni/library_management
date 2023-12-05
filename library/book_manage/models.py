from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=80)
    genre = models.CharField(max_length=70)
    isbn = models.IntegerField()
    availabile = models.CharField(max_length=20, default='Present')

    def __str__(self):
        return self.title

class Patron(models.Model):
    name= models.CharField(max_length=50, unique=True)
    phone_num = models.IntegerField(null= True)
    membership = models.BooleanField(default= False)

    def __str__(self):
        return self.name

class Borrow(models.Model):
    title = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.ForeignKey(Patron, on_delete=models.CASCADE)
    borrow_dt= models.DateField()
    return_dt =models.DateField()

    def __str__(self):
        return f"{self.title} => {self.name} => {self.borrow_dt}"