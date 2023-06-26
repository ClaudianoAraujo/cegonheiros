from django.shortcuts import render, redirect, get_object_or_404
from blog.models import BlogPost
from django.contrib.auth.models import User
from chapa.models import Chapa
from .forms import ChapaForm, CreateChapaForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_protect, csrf_exempt, requires_csrf_token
from django.contrib.auth.decorators import login_required



def base(request):
    pesq = BlogPost.objects.all()[:4]
    res = BlogPost.objects.last()
    context = {'res':res,
               'res2':pesq,
               }
    
    return render(request, 'index.html', context)


def detalhe(request,):
    pesquisa = Chapa.objects.last()
    pesquisa2 = Chapa.objects.all()[:8]
    context = {'chapa':pesquisa, 'chapa2':pesquisa2, 'link':'https://api.whatsapp.com/send?phone=55'}
    
    return render(request, 'detalhe.html', context)

@csrf_exempt
def register(request):
    return render(request, 'register.html')

@login_required
def profile(request, id):
    resp1 = User.objects.get(pk=id)
    resp = {'resp':resp1}
    return render(request, 'profile.html', resp)


@csrf_exempt
def create(request):
    if request.method == "POST" and  (request.POST['password'] == request.POST['password-conf']):
        user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
        user.last_name = request.POST['lastname']
        user.set_password = request.POST['username']
        user.save()
        return redirect('formlogin')
    
    
@csrf_exempt
def formes(request):
    form = ChapaForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('login2')
            
    context = {'form':form}
    return render(request, 'form.html', context)


@csrf_exempt
def create_chapa(request):
    form = CreateChapaForm(request.POST)
    if form.is_valid():
        form.save()
        info = request.POST['username']
        return redirect('profile', info)
               
    context = {'form':form}   
    return render(request, 'form.html', context)


@csrf_exempt
def formlogin(request):
    return render(request, 'login.html')


@csrf_exempt
def dologin(request):
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('profile', user.pk)
    else:
        return redirect('login')
    
@csrf_exempt    
def buscar(request):
    pesquisar = request.POST['param']
    busca = BlogPost.objects.filter(title__icontains=pesquisar)
    print(busca)
    print(request.POST['param'])
    resultado = {'pesquisa':busca}
    return render(request, 'post.html', resultado)

@csrf_exempt    
def buscar_chapa(request):
    pesquisar = request.POST['param']
    busca = Chapa.objects.filter(estado__icontains=pesquisar)
    print(busca)
    print(request.POST['param'])
    resultado = {'chapa_b':busca, 'link':'https://api.whatsapp.com/send?phone=55'}
    return render(request, 'detalhe.html', resultado)
        
    
    
    
    


        
        

            
        
            

