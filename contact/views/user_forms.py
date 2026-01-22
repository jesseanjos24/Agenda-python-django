from django.shortcuts import render, redirect
from contact.forms import ResgisterForm, RegisteUpdateForm
from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def register(request):
    
    form = ResgisterForm()
    
    '''messages.info(request, 'Welcome to the registration page.')
    messages.error(request, 'Não foi possível completar o registro.')
    messages.warning(request, 'Your password will expire in 7 days.')'''
    
    
    if request.method == 'POST':
        form = ResgisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration completed successfully!')
            return redirect('contact:login')
    else:
        form = ResgisterForm()
    
    context = {
        'form': form
    }
    
    return render(
        request,
        'contact/register.html',
        context,
    )
    
def login_view(request):
    
    form = AuthenticationForm(request)
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Login successful!')
            auth.login(request, user)
            return redirect('contact:index')
        messages.error(request, 'Invalid username or password.')
    
    context = {
        'form': form
    }
    return render(
        request,
        'contact/login.html',
        context,
    )
   
 
@login_required(login_url='contact:login')    
def logout_views(request):
    auth.logout(request)
    messages.info(request, 'You have been logged out successfully.')
    return redirect('contact:login')


@login_required(login_url='contact:login')
def user_update(request):
    form = RegisteUpdateForm(instance=request.user)
    
    if request.method == 'POST':
        form = RegisteUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated successfully!')
            return redirect('contact:index')
    
    context = {
        'form': form
    }
    
    return render(
        request,
        'contact/user-update.html',
        context,
    )