import json
import csv
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import RegistroHoraExtra
from .forms import RegistroHoraExtraForm
import xlwt


class HoraExtraList(ListView):
    model = RegistroHoraExtra

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)


class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    #fields = ['motivo', 'funcionario', 'horas']

    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEdit, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraEditBase(UpdateView):
    model = RegistroHoraExtra
    #fields = ['motivo', 'funcionario', 'horas']

    form_class = RegistroHoraExtraForm
    #success_url = reverse_lazy('list_hora_extra')

    def get_success_url(self):
        return reverse_lazy('update_hora_extra_base', args=[self.object.id])

    def get_form_kwargs(self):
        kwargs = super(HoraExtraEditBase, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('list_hora_extra')


class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    #fields = ['motivo', 'funcionario', 'horas']
    form_class = RegistroHoraExtraForm

    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs


class UtilizouHoraExtra(View):
    def post(self, *args, **kwargs):

        registro_hora_extra = RegistroHoraExtra.objects.get(id=kwargs['pk'])
        if self.request.POST.get('utilizou') == "True":
            registro_hora_extra.utilizada = True
        else:
            registro_hora_extra.utilizada = False
        registro_hora_extra.save()

        empregado = self.request.user.funcionario

        response = json.dumps(
            {'mensagem': 'requisição realizada',
            'horas': float(empregado.total_horas_extra)}
        )

        return HttpResponse(response, content_type='application/json')

class ExportarCsv(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] =  'attachment; filename="somefilename.csv"'

        registro_he = RegistroHoraExtra.objects.filter(utilizada=False)

        writer = csv.writer(response)
        writer.writerow(['ID', 'Motivo', 'Funcionario', 'Rest, Funcionario', 'Horas'])
        for registro in registro_he:
            writer.writerow([registro.id, registro.motivo, registro.funcionario,
                             registro.funcionario.total_horas_extra, registro.horas
                             ])

        return response

class ExportarExcel(View):
    def get(self, request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="relatorio_excel.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('banco de horas')

        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['id', 'Funcionario', 'motivo','Rest. Func', 'Horas']

        for col_num in range(len(columns)):
            ws.write(row_num,col_num, columns[col_num], font_style)

        font_style = xlwt.XFStyle()

        registros = RegistroHoraExtra.objects.filter(utilizada=False)

        row_num = 1
        for registro in registros:
            ws.write(row_num, 0, registro.id, font_style)
            ws.write(row_num, 1, registro.funcionario.nome, font_style)
            ws.write(row_num, 2, registro.motivo, font_style)
            ws.write(row_num, 3, registro.funcionario.total_horas_extra, font_style)
            ws.write(row_num, 4, registro.horas, font_style)
            row_num += 1

        wb.save(response)
        return response