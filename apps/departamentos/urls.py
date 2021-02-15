from django.urls import path
from .views import DepartamentosList, DepartamentoEdit, DepartamentoDelete, DepartamentoCreate

urlpatterns = [
    path('', DepartamentosList.as_view(), name='list_departamentos'),
    path('novo/', DepartamentoCreate.as_view(), name='create_departamento'),
    path('edit/<int:pk>/', DepartamentoEdit.as_view(), name='update_departamento'),
    path('delete/<int:pk>/', DepartamentoDelete.as_view(), name='delete_departamento'),
    ]