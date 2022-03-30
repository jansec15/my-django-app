from ast import Break
from django.shortcuts import render, HttpResponse
from admisiones.forms import ImportarPaciente
from admisiones.models import Paciente, TipoIdentificacion
# Create your views here.


def home(request):
    return render(request, 'home.html')


def admision(request):

    if request.method == 'POST':
        formulario = request.FILES['archivo']
        data = formulario.read().decode('utf-8')
        csv_data = data.split("\n")
        cont = 0
        dict = {cont: {}}
        for x in csv_data[1:101]:
            if ';' in x:
                fields = x.split(';')
            else:
                fields = x.split(',')
            # print(x.split(','))
            tipoId = list(TipoIdentificacion.objects.filter(
                nombre=fields[0]).values_list('acronimo', flat=True))
            try:
                tipo = tipoId[0]
            except:
                tipo = ''
            try:
                dict[cont] = {
                    'tipo_idenfiticacion': tipo,
                    'numero_identificacion': fields[1],
                    'nombre': fields[2],
                    'apellido': fields[3],
                    'sexo': fields[4],
                    'fecha_nacimiento': fields[5],
                    'telefono': fields[6],
                    'email': fields[7],
                    'pais_nacimiento': fields[8],
                    'pais_residencia': fields[9],
                    'direccion': fields[10],
                    'ocupacion': fields[11],
                    'tipo_sangre': fields[12]
                }
            except:
                print(fields)
            cont += 1
        # print(dict)
        miFormulario = ImportarPaciente()
        return render(request, 'admision.html', {'datos': dict.values(), 'form': miFormulario})
    else:
        miFormulario = ImportarPaciente()

    return render(request, 'admision.html', {'form': miFormulario})

def editar(request,dato):
    dato=dato
    document="%s" %(dato)
    return HttpResponse(document)
