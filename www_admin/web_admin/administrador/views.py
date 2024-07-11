from django.shortcuts import redirect, render
from .models import Usuarios



# Create your views here.
TEMPATES_DIRS=(
    'os.patch.join(BASE_DIR,"templates")'
)

# Create your views here.
def index(request):                    #  <<==========
    return render(request,"index.html")      #  <<==========

def listar(request):      
    users = Usuarios.objects.all()
    datos = {'usuarios' : users}
    return render(request,"crud_usuarios/listar.html",datos)


def agregar(request):
    if request.method == 'POST':
        if (request.POST.get('nombre') and 
            request.POST.get('apellido') and 
            request.POST.get('correo') and 
            request.POST.get('telefono') and 
            request.POST.get('f_nac')):
            user = Usuarios()
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.correo = request.POST.get('correo')
            user.telefono = request.POST.get('telefono')
            user.f_nac = request.POST.get('f_nac')
            user.save()
            return redirect('listar')  # Asegúrate de que 'listar' es el nombre correcto en urls.py
        else:
            return render(request, "crud_usuarios/agregar.html", {
                'error': 'Todos los campos son obligatorios.'
            })
    else:
        return render(request, "crud_usuarios/agregar.html")

def actualizar(request): 
    if request.method == 'POST':
        if (request.POST.get('id') and
            request.POST.get('nombre') and 
            request.POST.get('apellido') and 
            request.POST.get('correo') and 
            request.POST.get('telefono') and 
            request.POST.get('f_nac')):
            user_id_old = request.POST.get('id')
            user_old= Usuarios()
            user_old = Usuarios.objects.get(id = user_id_old)
            user = Usuarios()
            user.id = request.POST.get('id')
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.correo = request.POST.get('correo')
            user.telefono = request.POST.get('telefono')
            user.f_nac = request.POST.get('f_nac')
            user.f_registro = user_old.f_registro
            user.save()
            return redirect('listar')
    else:
        users = Usuarios.objects.all()
        datos = {'usuarios' : users}
        return render(request,"crud_usuarios/actualizar.html", datos)


def eliminar(request):    
    if request.method == 'POST':
        if request.POST.get('id'):
            id_a_borrar = request.POST.get('id')
            tupla = Usuarios.objects.get(id = id_a_borrar)
            tupla.delete()
            return redirect('listar')

    else:
        users = Usuarios.objects.all()
        datos = {'usuarios' : users}                
        return render(request,"crud_usuarios/eliminar.html", datos)

def actualizar2(request):                    #  <<==========
    return render(request,"crud_productos/actualizar2.html") 
def agregar2(request):                    #  <<==========
    return render(request,"crud_productos/agregar2.html") 
def listar2(request):                    #  <<==========
    return render(request,"crud_productos/listar2.html") 
def eliminar2(request):                    #  <<==========
    return render(request,"crud_productos/eliminar2.html") 