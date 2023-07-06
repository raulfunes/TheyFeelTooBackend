from django.urls import path, include

from . import views


urlpatterns = [
    path("", views.index, name="index"),
]

urlpatterns += [
    path("animal/create/", views.AnimalCreate.as_view(), name="animal_create"),
    path("animal/update/<pk>", views.AnimalUpdate.as_view(), name="animal_update"),
    path("animal/delete/<pk>", views.AnimalDelete.as_view(), name="animal_delete"),
]

urlpatterns += [
    path(
        "curiosidad/create/",
        views.CuriosidadCreate.as_view(),
        name="curiosidad_create",
    ),
    path(
        "curiosidad/update/<pk>",
        views.CuriosidadUpdate.as_view(),
        name="curiosidad_update",
    ),
    path(
        "curiosidad/delete/<pk>",
        views.CuriosidadDelete.as_view(),
        name="curiosidad_delete",
    ),
]

urlpatterns += [
    path("imagen/create/", views.ImagenCreate.as_view(), name="imagen_create"),
    path("imagen/update/<pk>", views.ImagenUpdate.as_view(), name="imagen_update"),
    path("imagen/delete/<pk>", views.ImagenDelete.as_view(), name="imagen_delete"),
]

urlpatterns += [
    path("consejo/create/", views.ConsejoCreate.as_view(), name="consejo_create"),
    path("consejo/update/<pk>", views.ConsejoUpdate.as_view(), name="consejo_update"),
    path("consejo/delete/<pk>", views.ConsejoDelete.as_view(), name="consejo_delete"),
]

urlpatterns += [
    path(
        "habitats/",
        views.HabitatListView.as_view(),
        name="habitat_list",
    ),
    path(
        "habitat/create/",
        views.HabitatCreate.as_view(),
        name="habitat_create",
    ),
    path(
        "habitat/update/<pk>",
        views.HabitatUpdate.as_view(),
        name="habitat_update",
    ),
    path(
        "habitat/delete/<pk>",
        views.HabitatDelete.as_view(),
        name="habitat_delete",
    ),
]
