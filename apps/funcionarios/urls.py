from django.contrib import admin
from django.urls import path
from .views import FuncionariosList, FuncionarioEdit, FuncionarioDelete, FuncionarioCreate, relatorio_funcionarios, Pdf

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list_funcionarios'),
    path('novo/', FuncionarioCreate.as_view(), name='create_funcionario'),
    path('edit/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionarios'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('relatorio_funcionarios', relatorio_funcionarios, name='relatorio_funcionarios'),
    path('relatorio_funcionarios_html', Pdf.as_view(), name='relatorio_funcionarios_html'),
    ]
