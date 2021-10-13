from django.contrib.auth.decorators import login_required
from django.core import paginator
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from app.forms import CarrosForm, VendedoresForm
from app.models import Carros, Vendedores
from django.core.paginator import Paginator
from django.core.files.storage import FileSystemStorage


def display_images(request): 
  # getting all the objects of hotel. 
    allimages = Carros.objects.all()  
    return render(request, 'index',{'images' : allimages})

def display_images(request): 
  # getting all the objects of hotel. 
    allimages = Vendedores.objects.all()  
    return render(request, 'index',{'images' : allimages})


@login_required
def home(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Carros.objects.filter(modelo__icontains=search)
    else:
        data['db'] = Carros.objects.all()

   #data['db'] = Carros.objects.all()
   # all = Carros.objects.all()
   # paginator = Paginator(all, 5)
   # pages = request.GET.get('page')
   # data ['db'] = paginator.get_page(pages)

    return render (request, 'index.html', data)
    
@login_required 
def form(request):
     data = {}
     data ['form'] = CarrosForm()
     return render (request, 'form.html', data)



@login_required
def bloqueartela(request):
    return render(request, 'bloqueartela.html')


@login_required
def base(request):
    return render(request,'base.html')

@login_required
def general(request):
    data= {}
    return render(request, 'general.html')

@login_required
def cadvendedores(request):
    data = {}
    data ['cadvendedores'] = VendedoresForm()
    return render (request, 'cadvendedores.html', data)

@login_required
def createvendedores(request):
        if request.method == 'POST':
            form = VendedoresForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('sucesso')
        else:
            form = VendedoresForm()
        return render(request, 'cadvendedores.html', {
            'form': form
        })






@login_required
def create(request):
    if request.method == 'POST':
        form = CarrosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = CarrosForm()
    return render(request, 'form.html', {
        'form': form
    })

def sucesso(request):
    return HttpResponse('Sucesso!!!')


# def create(request):
#     form = CarrosForm(request.POST, request.FILES)
#     if form.is_valid():
#         form.save()
#         return redirect('form')

def display_image(request):
    if request.method =='GET':
        carros = Carros.objects.all()
        return render ((request, '/', {Carros : Carros }))


@login_required
def vendedores(request):
    data = {}
    search = request.GET.get('search')
    if search:
        data['db'] = Vendedores.objects.filter(nome__icontains=search)
    else:
        data['db'] = Vendedores.objects.all()
    return render(request, 'vendedores.html', data)




@login_required
def view (request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    return render(request, 'view.html', data)

@login_required
def edit (request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    data['form'] = CarrosForm(instance=data['db'])
    return render(request, 'form.html', data )

@login_required
def update(request, pk):
    data = {}
    data['db'] = Carros.objects.get(pk=pk)
    form = CarrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect ('home')

@login_required
def delete(request, pk):
    db = Carros.objects.get(pk=pk)
    db.delete()
    return redirect('home')



