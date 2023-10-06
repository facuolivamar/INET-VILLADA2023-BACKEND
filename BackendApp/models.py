from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    groups = models.ManyToManyField(
        Group, verbose_name=("groups"), blank=True, related_name="custom_users"
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=("user permissions"),
        blank=True,
        related_name="custom_users",
    )
    class Meta:
        verbose_name_plural = "Usuarios"
        verbose_name = "Usuario"

class BloodType(models.Model):
    bloodType = models.CharField(max_length=255)
    def __str__(self):
        return str(self.bloodType)

    class Meta:
        verbose_name_plural = "Tipos de sangre"
        verbose_name = "Tipo de sangre"

class SocialPlan(models.Model):
    socialPlan = models.CharField(max_length=255)
    def __str__(self):
        return str(self.socialPlan)

    class Meta:
        verbose_name_plural = "Planes sociales"
        verbose_name = "Plan social"

class Room(models.Model):
    quantity_beds = models.IntegerField()
    room_number = models.IntegerField()
    def __str__(self):
        return str(self.room_number)

    class Meta:
        verbose_name_plural = "Ubicaciones"
        verbose_name = "Ubicacion"

class Doctor(CustomUser):
    specialty = models.CharField(max_length=255)

    def __str__(self):
        return str(self.first_name)

    class Meta:
        verbose_name_plural = "Doctores"
        verbose_name = "Doctor"


class Calls(models.Model):
    class TypeComboBox(models.TextChoices):
        NORMAL = 'Normal', 'Normal',
        EMERGENCY = 'Emergencia', 'Emergencia'
    
    type = models.CharField(
        max_length=30,
        choices=TypeComboBox.choices,
        default=TypeComboBox.NORMAL,
        verbose_name="Tipo",
    )

    class StateComboBox(models.TextChoices):
        ATTENDANCE = 'Atendido', 'Atendido',
        NOT_ATTENDANCE = 'No atendido', 'No atendido'
    
    state = models.CharField(
        max_length=30,
        choices=StateComboBox.choices,
        default=StateComboBox.NOT_ATTENDANCE,
        verbose_name="Estado",
    )

    attendance_date = models.DateTimeField()
    creation_date = models.DateTimeField()
    user_create_call = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='calls_created')
    user_response_call = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='calls_responded')
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural = "Llamadas"
        verbose_name = "Llamada"

class Patient(CustomUser):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    bloodType = models.ForeignKey(BloodType, on_delete=models.CASCADE)
    socialPlan = models.ForeignKey(SocialPlan, on_delete=models.CASCADE)
    height = models.FloatField()
    weight = models.FloatField()
    
    def __str__(self):
        return str(self.first_name)

    class Meta:
        verbose_name_plural = "Cursos"
        verbose_name = "Curso"
