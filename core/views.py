from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string

from .models import Medico
from .forms import MedicoForm


def medicos_list(request):
    template_name = "medicos_list.html"
    medicos = Medico.objects.all()
    context = {'medicos': medicos}
    return render(request, template_name, context)


def medicos_create(request):
    template_name = 'includes/crear_medicos.html'
    if request.method == 'POST':
        form = MedicoForm(request.POST)
    else:
        form = MedicoForm()
    return save_medicos_form(request, form, template_name)


def save_medicos_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        data['form_is_valid'] = True
        medicos = Medico.objects.all()
        data['html_medicos_list'] = render_to_string('includes/lista_medicos.html', {'medicos': medicos})
    else:
        data['form_is_valid'] = False
    context = {'form': form}
    # le Envio al modal los controles del form
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def medicos_update(request, pk):
    template_name = 'includes/actualizar_medicos.html'
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        form = MedicoForm(request.POST, instance=medico)
    else:
        form = MedicoForm(instance=medico)
    return save_medicos_form(request, form, template_name)


def medicos_delete(request, pk):
    template_name = 'includes/eliminar_medico.html'
    data = dict()
    medico = get_object_or_404(Medico, pk=pk)
    if request.method == 'POST':
        medico.delete()
        data['form_is_valid'] = True
        medicos = Medico.objects.all()
        data['html_medicos_list'] = render_to_string('includes/lista_medicos.html', {'medicos': medicos})
    else:
        context = {'medico': medico}
        data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)