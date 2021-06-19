from django.contrib import admin
from .models import Student, Note, Curs

admin.site.register(Note)
admin.site.register(Curs)
# Register your models here.

class NotaInline(admin.TabularInline):
    model = Note


class StudentAdmin(admin.ModelAdmin):
    #list-view specific customizations
    list_per_page = 10
    search_fields = ('nume', 'prenume')
    list_filter = ('an', 'cursuri')
    list_display = ('nume', 'prenume', 'an')
    #changeview customizations
    fieldsets = [
        ('', {
            'fields': ['prenume', 'nume']
         }
        ),
        ('Date Scolare', {
            'fields': ['cursuri', 'an'],
            'classes': ['collapse']
        })
    ]
    inlines = (NotaInline, )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.none()
        return qs
    
admin.site.register(Student, StudentAdmin)