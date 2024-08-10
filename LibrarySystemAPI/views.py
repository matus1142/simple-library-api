from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Member, Book, Loan
from .serializers import MemberSerializer, BookSerializer, LoanSerializer

class MemberListCreateView(generics.ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class MemberDetailView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class LoanListCreateView(generics.ListCreateAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

class LoanDetailView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer