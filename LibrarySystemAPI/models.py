from django.db import models

# Create your models here.

# Member Model
class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    membership_start_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Book Model
class Book(models.Model):
    title = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    author = models.CharField(max_length=100)
    copies_available = models.IntegerField()

    def __str__(self):
        return self.title

# Loan Model
class Loan(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Loan: {self.book.title} to {self.member.first_name} {self.member.last_name}"
