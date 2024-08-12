from django.contrib import admin

from LibrarySystemAPI.models import Book, Loan, Member

# Register your models here.
admin.site.register([Member,Book,Loan])