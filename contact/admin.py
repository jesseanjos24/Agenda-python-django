from django.contrib import admin
from contact.models import Contact, Category

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'created_date')
    ordering = ('-created_date',)
    search_fields = ('id', 'first_name', 'last_name', 'email', 'phone')
    list_per_page = 20
    list_max_show_all = 150
    #list_editable = ('phone',) - exemplo de campo editavel na listagem
    #list_display_links = ('first_name', 'last_name') - exemplo de link para editar
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name'),
    ordering = '-id',
    
