from django.contrib import admin
from myapp.models import Comunicado, Entidad


class ComunicadoAdmin (admin.ModelAdmin):

    readonly_fields = ('publicado_por' , 'modificado_por', 'entidad', )

    def save_model(self, request, obj, form, change):
        usuario = request.user
        entity = Entidad.objects.filter(administrador=usuario).first()
        obj.entidad = entity
        if not obj.publicado_por:
            obj.publicado_por = usuario
        obj.modificado_por = usuario
        super(ComunicadoAdmin, self).save_model(request,obj,form,change)

    def get_queryset(self, request):
        qs = super(ComunicadoAdmin, self).get_queryset(request)
        qs = qs.filter(publicado_por=request.user)
        return qs
    
admin.site.register(Comunicado, ComunicadoAdmin)
admin.site.register(Entidad)