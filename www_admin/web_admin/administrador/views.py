from django.shortcuts import redirect, render
from .models import Usuarios
from .models import Productos



# Create your views here.
TEMPATES_DIRS=(
    'os.patch.join(BASE_DIR,"templates")'
)

# INDEX PRINCIPAL.
def index(request):                    #  <<==========
    return render(request,"index.html")      #  <<==========

# INDEX FORNITE.
def indexF(request):                    #  <<==========
    return render(request,"indexF.html")  

# INDEX GTA V ONLINE
def indexgta(request):                    #  <<==========
    return render(request,"indexgta.html")  

# INDEX FORMULARIO
def indexform(request):
    return render(request,"indexform.html") 


# CRUD 

#L-I-S-T-A-R

# LISTAR USUARIOS 
def listar(request):      
    users = Usuarios.objects.all()
    datos = {'usuarios' : users}
    return render(request,"crud_usuarios/listar.html",datos)

# LISTAR PRODUCTOS 
def listar2(request): 
    prod = Productos.objects.all()
    datos2 = {'productos': prod}                   
    return render(request,"crud_productos/listar2.html",datos2) 

#A-G-R-E--G-A-R

# AGREGAR USUARIOS 
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
            return redirect('listar')  
        else:
            return render(request, "crud_usuarios/agregar.html", {
                'error': 'Todos los campos son obligatorios.'
            })
    else:
        return render(request, "crud_usuarios/agregar.html")

# AGREGAR PRODUCTOS  /user= prod
def agregar2(request):   
    if request.method == 'POST':
        if (request.POST.get('nombre2') and 
            request.POST.get('precio2')):
            prod = Productos()
            prod.nombre2 = request.POST.get('nombre2')
            prod.precio2 = request.POST.get('precio2')
            prod.save()
            return redirect('listar2')  
        else:
            return render(request, "crud_productos/agregar2.html", {
                'error': 'Todos los campos son obligatorios.'
            })
    else:              
        return render(request,"crud_productos/agregar2.html") 

#A-C-T-U-A-L-I-Z-A-R

# ACTUALIZAR USUARIOS
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

# ACTUALIZAR PRODUCTOS
def actualizar2(request): 
    if request.method == 'POST':
        if (request.POST.get('id2') and
            request.POST.get('nombre2') and 
            request.POST.get('precio2')):
            prod_id_old2 = request.POST.get('id2')
            prod_old2 = Productos()
            prod_old2 = Productos.objects.get(id2 = prod_id_old2)
            prod = Productos()
            prod.id2 = request.POST.get('id2')
            prod.nombre2 = request.POST.get('nombre2')
            prod.precio2 = request.POST.get('precio2')
            prod.f_registro2 = prod_old2.f_registro2
            prod.save()
            return redirect('listar2')
    else:
        prod = Productos.objects.all()
        datos2 = {'productos' : prod}
        return render(request,"crud_productos/actualizar2.html", datos2)

#E-L-I-M-I-N-A-R

#ELIMINAR USUARIOS
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

#ELIMINAR PRODUCTOS
def eliminar2(request): 
    if request.method == 'POST':
        if request.POST.get('id2'):
            id_a_borrar2 = request.POST.get('id2')
            tupla = Productos.objects.get(id2 = id_a_borrar2)
            tupla.delete()
            return redirect('listar2')

    else:
        prod = Productos.objects.all()
        datos2 = {'productos' : prod}                               
        return render(request,"crud_productos/eliminar2.html",datos2) 

