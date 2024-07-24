# API/teneastapi/teneastapp/urls.py
from django.urls import path
from .views import InquiryCreateView, InquiryListView, InquiryDetailView, LoginView, RegisterView

urlpatterns = [
    path('inquire/', InquiryCreateView.as_view(), name='inquire'),
    path('inquiries/', InquiryListView.as_view(), name='inquiry-list'),
    path('inquiries/<int:pk>/', InquiryDetailView.as_view(), name='inquiry-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
]