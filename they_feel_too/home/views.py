from django.shortcuts import render
from .models import Animal, Consejo, Curiosidad, Habitat, Imagen

# Create your views here.


def index(request):
    """
    Funcion vista para la página inicio del sitio.
    """

    animales = Animal.objects.all()[:4]
    curiosidades = Curiosidad.objects.all()
    consejos = Consejo.objects.all()

    imagenes = Imagen.objects.all()

    return render(
        request,
        "index.html",
        context={
            "animales": animales,
            "consejos": consejos,
            "curiosidades": curiosidades,
            "imagenes": imagenes,
        },
    )


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views import generic


class HabitatListView(PermissionRequiredMixin, generic.ListView):
    permission_required = "home.is_admin"
    model = Habitat
    paginate_by = 10


class AnimalCreate(PermissionRequiredMixin, CreateView):
    permission_required = "home.is_admin"
    model = Animal
    fields = "__all__"
    success_url = reverse_lazy("index")


class AnimalUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = "home.is_admin"
    model = Animal
    fields = "__all__"
    success_url = reverse_lazy("index")


class AnimalDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "home.is_admin"
    model = Animal
    success_url = reverse_lazy("index")


class CuriosidadCreate(PermissionRequiredMixin, CreateView):
    permission_required = "home.is_admin"
    model = Curiosidad
    fields = "__all__"
    success_url = reverse_lazy("index")


class CuriosidadUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = "home.is_admin"
    model = Curiosidad
    fields = "__all__"
    success_url = reverse_lazy("index")


class CuriosidadDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "home.is_admin"
    model = Curiosidad
    success_url = reverse_lazy("index")


class ImagenCreate(PermissionRequiredMixin, CreateView):
    permission_required = "home.is_admin"
    model = Imagen
    fields = "__all__"
    success_url = reverse_lazy("index")


class ImagenUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = "home.is_admin"
    model = Imagen
    fields = "__all__"
    success_url = reverse_lazy("index")


class ImagenDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "home.is_admin"
    model = Imagen
    success_url = reverse_lazy("index")


class ConsejoCreate(PermissionRequiredMixin, CreateView):
    permission_required = "home.is_admin"
    model = Consejo
    fields = "__all__"
    success_url = reverse_lazy("index")


class ConsejoUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = "home.is_admin"
    model = Consejo
    fields = "__all__"
    success_url = reverse_lazy("index")


class ConsejoDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "home.is_admin"
    model = Consejo
    success_url = reverse_lazy("index")


class HabitatCreate(PermissionRequiredMixin, CreateView):
    permission_required = "home.is_admin"
    model = Habitat
    fields = "__all__"
    success_url = reverse_lazy("index")


class HabitatUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = "home.is_admin"
    model = Habitat
    fields = "__all__"
    success_url = reverse_lazy("index")


class HabitatDelete(PermissionRequiredMixin, DeleteView):
    permission_required = "home.is_admin"
    model = Habitat
    success_url = reverse_lazy("index")
