from django.shortcuts import render
from contact.forms import ContactForm


# Create your views here.
def create(request):
    
    if request.method == 'POST':
        
        context = {
            'form': ContactForm(request.POST or None)
        }
        
        return render(
            request,
            'contact/create.html',
            context,
        )
        
    context = {
            'form': ContactForm()
        }
        
    return render(
        request,
        'contact/create.html',
        context,
    )