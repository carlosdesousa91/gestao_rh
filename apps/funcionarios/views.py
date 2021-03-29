from django.contrib.auth.models import User
from django.http import HttpResponse, FileResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView, View, TemplateView
from .models import Funcionario
import io
from reportlab.pdfgen import canvas
from django.template.loader import get_template
from xhtml2pdf import pisa


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        return Funcionario.objects.filter(empresa=empresa_logada)


class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos']


class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('list_funcionarios')


class FuncionarioCreate(CreateView):
    model = Funcionario
    fields = ['nome', 'departamentos']

    def form_valid(self, form):
        funcionario = form.save(commit=False)
        username = funcionario.nome.split(' ')[0] + funcionario.nome.split(' ')[1]
        funcionario.empresa = self.request.user.funcionario.empresa
        funcionario.user = User.objects.create(username=username)
        funcionario.save()
        return super(FuncionarioCreate, self).form_valid(form)


def relatorio_funcionarios(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
    
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(10, 810, 'Relatório de funcionarios')

    funcionarios = Funcionario.objects.filter(empresa=request.user.funcionario.empresa)

    str_ = 'Nome: %s | Hora Extra %.2f'

    y = 790
    for funcionario in funcionarios:
        p.drawString(10, y, str_ % (funcionario.nome, funcionario.total_horas_extra))
        y -= 40

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    #buffer.seek(0)
    return response

class Render:
  @staticmethod
  def render(path:str, params: dict, filename:str):
    template = get_template(path)
    html = template.render(params)
    response = io.BytesIO()
    pdf = pisa.pisaDocument(
      io.BytesIO(html.encode("UTF-8")), response)
    if not pdf.err:
      response = HttpResponse(
        response.getvalue(), content_type='application/pdf')
      response['Content-Disposition'] = 'attachment; filename=%s.pdf' % filename
      return response
    else:
      return HttpResponse("Error Rendering PDF", status=400)

class Pdf(View):

  def get(self, request):
    params = {
      'today': 'Variavel today',
      'sales': 'Variavel sales',
      'request': request,
    }
    return Render.render('funcionarios/relatorio.html', params, 'myfile')

class Pdf_debug(TemplateView):
    params = {
        'today': 'Variavel today',
        'sales': 'Variavel sales',

    }
    template_name = 'funcionarios/relatorio.html';

    def get_context_data(self, **kwargs):
        params = {
            'today': 'Variavel today',
            'sales': 'Variavel sales',

        }
        return params
