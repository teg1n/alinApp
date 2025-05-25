from django.contrib import admin
from sharingApp.models import Share

class SharingAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Mesaj Grubu', {"fields": ["content"]}),  
        ('Kullanıcı Grubu', {"fields": ["user"]}),  
        ('Tarih Bilgisi', {"fields": ["created_at"]}),
        ('Durum', {"fields": ["deleted"]}),  
        ('Fotoğraf', {"fields": ["foto"]}),
    ]
    list_display = ('user', 'content', 'created_at', 'deleted', 'foto')  
    search_fields = ('content', 'user__username')
    list_filter = ('created_at', 'deleted')  

admin.site.register(Share, SharingAdmin)
