from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from contact.models import Contact
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    contacts = Contact.objects.filter(show=True).order_by('-id')
    
    paginador = Paginator(contacts, 20)
    page_number = request.GET.get("page")
    page_obj = paginador.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'site_title': 'Contatos - '
    }
    
    return render(
        request,
        'contact/index.html',
        context,
    )   

def search(request):
    
    search_term = request.GET.get('q', '').strip()
    
    if search_term == '':
        return redirect('contact:index')
        
    contacts = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=search_term)|
        Q(last_name__icontains=search_term) |
        Q(email__icontains=search_term) |
        Q(phone__icontains=search_term)
    ).order_by('-id')
    
    paginador = Paginator(contacts, 20)
    page_number = request.GET.get("page")
    page_obj = paginador.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'site_title': 'Busca 🔎- ',
        'search_term': search_term,
    }
    
    return render(
        request,
        'contact/index.html',
        context,
    )

    
def contact(request, contact_id):
    #single_contact = Contact.objects.filter(pk=contact_id).first()
    
    single_contact = get_object_or_404(Contact, pk=contact_id, show=True)
    
    contact_name = f'{single_contact.first_name} {single_contact.last_name}'
    
    #if single_contact is None:
    #    raise Http404("Contact does not exist")
    
    context = {
        'contact': single_contact,
        'site_title': f'{contact_name} - '
    }
    
    return render(
        request,
        'contact/contact.html',
        context,
    )

