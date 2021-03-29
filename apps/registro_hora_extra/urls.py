from django.urls import path
from .views import HoraExtraList, HoraExtraEdit, HoraExtraEditBase, \
    HoraExtraDelete, HoraExtraCreate, UtilizouHoraExtra, ExportarCsv, ExportarExcel

urlpatterns = [
    path('', HoraExtraList.as_view(), name='list_hora_extra'),
    path('novo/', HoraExtraCreate.as_view(), name='create_hora_extra'),
    path('edit-funcionario/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
    path('edit/<int:pk>/', HoraExtraEditBase.as_view(), name='update_hora_extra_base'),
    path('utilizou-hora-extra/<int:pk>/', UtilizouHoraExtra.as_view(), name='utilizou_hora_extra'),
    path('delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('exportar_csv', ExportarCsv.as_view(), name='exportar_csv'),
    path('exportar_excel', ExportarExcel.as_view(), name='exportar_excel'),

    ]
