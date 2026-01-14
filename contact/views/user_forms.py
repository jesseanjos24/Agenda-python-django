from django.shortcuts import render, redirect
from contact.forms import ResgisterForm

def register(request):
    
    form = ResgisterForm()
    
    if request.method == 'POST':
        form = ResgisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact:register')
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