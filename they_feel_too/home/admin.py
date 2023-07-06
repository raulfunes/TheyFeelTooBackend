from django.contrib import admin

# Register your models here.

from .models import Animal, Consejo, Curiosidad, Habitat, Imagen


@admin.register(Habitat)
class HabitatAdmin(admin.ModelAdmin):
    list_display = ("nombre", "continente")


@admin.register(Animal)
class AnimalAdmmin(admin.ModelAdmin):
    list_display = ("nombre", "display_habitats", "alimentacion")
    list_filter = ("alimentacion",)


admin.site.register(Consejo)
admin.site.register(Curiosidad)
admin.site.register(Imagen)
