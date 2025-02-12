from django.shortcuts import render , redirect
from . import models 
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm ,CustomAuthenticationForm , ShareForm
from django.contrib.auth import login, authenticate ,logout
from .models import Share
from django.shortcuts import *
from django.contrib import messages


# Create your views here.

def login_view(request):
    if request.user.is_authenticated:  
        return redirect(reverse('sharingApp:ui'))
    
    if request.method == "POST":
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('sharingApp:ui'))
            else:
                form.add_error(None, "Kullanıcı adı veya şifre hatalı!")  
    else:
        form = CustomAuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return(redirect('/login/'))


@login_required
def ui(request):

    all_sharings = models.Share.objects.filter(deleted=False).order_by('-created_at') 
    sharing_dict = {"showsharings": all_sharings}

    if request.method == 'POST':
        form = ShareForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')

            if len(content) > 150:
                form.add_error('content', 'Maksimum 150 karakter girebilirsiniz.')
            else:
                new_sharing = form.save(commit=False)
                new_sharing.user = request.user
                new_sharing.save()  
                return redirect('/')  

    else:
        form = ShareForm()

    sharing_dict['form'] = form  
    return render(request, 'sharingApp/home.html', context=sharing_dict)

@login_required
def share_form(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        Share.objects.create(user=request.user, content=content)
        return redirect('/') 
    return redirect('/')
    
def register(request):
    if request.user.is_authenticated:
        return(redirect('/'))

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def deletetext(request,id):
    texts= get_object_or_404(Share,pk=id)
    if request.user == texts.user:
        texts.deleted = True  
        texts.save()
        messages.success(request,"Paylaşım başarıyla silindi")

    else:
        messages.error(request,"Bir sorun oluştu")
    
    return redirect('sharingApp:ui')