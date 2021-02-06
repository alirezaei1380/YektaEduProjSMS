from django.urls import path
from . import views

urlpatterns = [
    path('form', views.FormView.as_view(), name='form'),
    path('success', views.success_view, name='success')
]
