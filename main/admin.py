from django.contrib import admin
from .models import Project, Personnel, Detail, Service, Equipe

# to show the id column
class idAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)

admin.site.register(Project,idAdmin)
admin.site.register(Personnel,idAdmin)
admin.site.register(Equipe,idAdmin)
admin.site.register(Detail,idAdmin)
admin.site.register(Service,idAdmin)



