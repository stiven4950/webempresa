from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

    def get_readonly_fields(self, request, obj = None):
        if request.user.groups.filter(name = 'Personal').exists():
            return ('created','updated', 'key', 'name')
            #return ('key', 'name') # Si se quita el resto de los campos entonces no se mostrarán
        else:
            return ('created', 'updated')


admin.site.register(Link, LinkAdmin)