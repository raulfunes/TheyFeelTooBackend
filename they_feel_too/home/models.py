from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid

# Create your models here.


class Habitat(models.Model):
    """
    Modelo que representa un habitat
    """

    CONTINENTE = [
        ("AF", "Africa"),
        ("AS", "Asia"),
        ("AM", "America"),
        ("EU", "Europa"),
        ("OC", "Oceania"),
        ("AN", "Antartida"),
        ("M", "Mundo"),
    ]

    nombre = models.CharField(max_length=100)
    continente = models.CharField(max_length=2, choices=CONTINENTE)

    def __str__(self):
        """
        String que representa al objeto Habitat
        """
        return f"{self.nombre}, {self.continente}"

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular del Habitat
        """
        return reverse("habitat_detail", args=[str(self.id)])


class Animal(models.Model):
    """
    Modelo que representa un animal
    """

    nombre = models.CharField(max_length=100)
    promedio_de_vida = models.CharField(
        max_length=100, help_text="Puede escribir tanto en cautiverio como salvaje"
    )
    alimentacion = models.CharField(
        max_length=100, help_text="En que se basa la alimentación del animal"
    )
    imagen = models.CharField(max_length=100, help_text="Link a la imagen del animal")
    habitats = models.ManyToManyField(
        Habitat, help_text="Habitats a los que pertenece el animal"
    )

    class Meta:
        ordering = ["nombre"]
        permissions = (("is_admin", "Can administrate"),)

    def __str__(self):
        """
        String que representa al objeto Animal
        """
        return self.nombre

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular del Animal
        """
        return reverse("animal_detail", args=[str(self.id)])

    def display_habitats(self):
        return ", ".join(
            {
                f"{habitat.nombre} ({habitat.continente})"
                for habitat in self.habitats.all()[:3]
            }
        )

    display_habitats.short_description = "habitat"


class Curiosidad(models.Model):
    """
    Modelo que representa una curiosidad
    """

    nombre = models.TextField(
        max_length=200,
        help_text="Curiosidad del animal",
    )
    animal = models.ForeignKey(
        Animal,
        help_text="Animal al que pertenece esta curiosidad",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        """
        String que representa al objeto Curiosidad
        """
        return self.nombre

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de la curiosidad
        """
        return reverse("curiosidad_detail", args=[str(self.id)])


class Consejo(models.Model):
    """
    Modelo que representa un consejo
    """

    nombre = models.CharField(
        max_length=200,
        help_text="Consejos para preservar la flora y fauna del planeta",
    )

    def __str__(self):
        """
        String que representa al objeto Consejo
        """
        return self.nombre

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de la Consejo
        """
        return reverse("consejo_detail", args=[str(self.id)])


class Imagen(models.Model):
    """
    Modelo que representa una imagen
    """

    alt = models.CharField(
        max_length=200, help_text="Texto auxiliar por si la imagen se encuentra caida"
    )

    ESTILOS = [("img-larga", "img-larga"), ("img-corta", "img-corta")]

    estilo = models.CharField(
        max_length=100,
        choices=ESTILOS,
        help_text="Tamaño con el que se mostrara la imagen",
    )

    imagen = models.TextField(help_text="Link a la imagen")

    def __str__(self):
        """
        String que representa al objeto Imagen
        """
        return self.alt

    def get_absolute_url(self):
        """
        Devuelve el URL a una instancia particular de la Imagen
        """
        return reverse("imagen_detail", args=[str(self.id)])
