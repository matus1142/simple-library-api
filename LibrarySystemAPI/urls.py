
from django.urls import path,include

from LibrarySystemAPI import views

urlpatterns = [
    path('members/', views.MemberListCreateView.as_view(), name='member-list'),
    path('members/<int:pk>/', views.MemberDetailView.as_view(), name='member-detail'),
    path('books/', views.BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('loans/', views.LoanListCreateView.as_view(), name='loan-list'),
    path('loans/<int:pk>/', views.LoanDetailView.as_view(), name='loan-detail'),
]
