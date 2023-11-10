from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
from .decorators import user_not_authenticated

# Create your views here.


User = get_user_model()

@user_not_authenticated
def register(request):
    # User = get_user_model()
    template = 'register.html'
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = RegisterForm()

    return render(request, template, {"form": form})


@user_not_authenticated
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        # user = auth.authenticate(username=username, password=password)
        if user is not None:
            # login(request, user)
            login(request, user)
            messages.success(request, f'Welcome <strong>{username}</strong>')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')



# Costom form validation from the Backend

# def register(FormView):
    
    # if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     password2 = request.POST['password2']
        
    #     if password == password2:
    #         if User.objects.filter(email=email).exists():
    #             messages.error(request, 'Email Already used')
    #             return redirect('register')
    #         elif User.objects.filter(username=username).exists():
    #             messages.error(request, 'Username Already Used')
    #             return redirect('register')
    #         else:
    #             user = User.objects.create_user(username=username, email=email, password=password)
    #             user.save()
    #             return redirect('login')
    #     else:
    #         messages.success(request, 'Passwords Not The Same')
    #         return redirect('register')
    # else:
    #     return render(request, 'dashboard/register.html')



def check_username(request):
    username = request.POST.get('username')

    forbidden_user = ['admin', 'css', 'js', 'authenticate', 'login', 'logout', 'administrator', 'root', 'email', 'user', 'join', 'sql', 'static', 'python']
    
    if username.lower() in forbidden_user:
        return HttpResponse('<div style="color: red;">The username entered is prohibited. Please try another one</div> <i class="fas fa-exclamation-circle failure-icon"></i>')
    
    
    if '@' in username or '+' in username or '-' in username or ',' in username or '.' in username or '?' in username or '()' in username or '#' in username or '*' in username or '$' in username or '%' in username:
        return HttpResponse(f'<div style="color: red;"><b>{username}</b> is an invalid username. Special characters not allowed</div> <i class="fas fa-exclamation-circle failure-icon"></i>')

    try:
        if User.objects.filter(username=username).exists():
            return HttpResponse(f'<div style="color: red;">Username {username} already exists</div> <i class="fas fa-exclamation-circle failure-icon"></i>')
        else:
            return HttpResponse()
    except:
        pass
      
    
    
    
    

def check_email(request):
    email = request.POST['email']
    
    if User.objects.filter(email=email).exists():
        return HttpResponse(f'<div style="color: red;">User with <b>{email}</b> already exists</div> <i class="fas fa-exclamation-circle failure-icon"></i>')
    else:
        return HttpResponse()


    
    
def check_password(request):
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    if not password1 == password2:
        return HttpResponse('<div style="color: red;">Passwords don\'t match</div> <i class="fas fa-exclamation-circle failure-icon"></i>')
    elif password1 and password2 == '':
        return HttpResponse()
    else: return HttpResponse()



    
    

