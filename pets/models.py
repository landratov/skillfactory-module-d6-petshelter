import uuid

from django.db import models
from django.core import validators


class Type(models.Model):
    """Type description"""

    name = models.CharField(max_length=30, verbose_name="Вид")

    class Meta:
        verbose_name = "Вид"
        verbose_name_plural = "Виды"

    def __str__(self):
        return self.name


class Breed(models.Model):
    """Breed description"""

    type = models.ForeignKey('pets.Type', on_delete=models.CASCADE, verbose_name="Вид")
    name = models.CharField(max_length=255, verbose_name="Порода")
    code = models.CharField(max_length=255, verbose_name="Код")

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"

    def __str__(self):
        return self.name


class Pet(models.Model):
    """Pet description"""

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    type = models.ForeignKey('pets.Type', on_delete=models.CASCADE, verbose_name="Вид")
    breed = models.ForeignKey('pets.Breed', on_delete=models.CASCADE, verbose_name="Порода")
    name = models.CharField(max_length=100, verbose_name="Кличка")
    age = models.PositiveSmallIntegerField(verbose_name="Возраст", validators=[validators.MaxValueValidator(150)])
    description = models.TextField(verbose_name="Описание")
    photo = models.ImageField(upload_to="photos", verbose_name="Фото", null=True, blank=True)

    class Meta:
        verbose_name = "Питомец"
        verbose_name_plural = "Питомцы"

    def __str__(self):
        return self.name
