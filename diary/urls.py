from django.urls import path
from . import views

app_name = 'diary'
urlpatterns = [
    path('', views.IndexVIew.as_view(), name="index"),
    path('inquiry/', views.InquiryVIew.as_view(), name="inquiry"),
]
