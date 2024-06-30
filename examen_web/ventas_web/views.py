from django.shortcuts import render

def index(request):
    return render(request, 'ventas_web/index.html')

def cash_gta(request):
    return render(request, 'ventas_web/Cash_gta.html')

def crud_empleado(request):
    return render(request, 'ventas_web/crudempleado.html')

def formulario_contacto(request):
    return render(request, 'ventas_web/formulario-contacto.html')

def fornite(request):
    return render(request, 'ventas_web/Fornite.html')

def index_login(request):
    return render(request, 'ventas_web/indexLogin.html')

def nosotros(request):
    return render(request, 'ventas_web/nosotros.html')

def recuperar_contrasena(request):
    return render(request, 'ventas_web/recuperarC.html')

def rp_riot(request):
    return render(request, 'ventas_web/Rp_riot.html')

def signup(request):
    return render(request, 'ventas_web/signup.html')
