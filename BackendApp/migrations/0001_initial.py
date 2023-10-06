# Generated by Django 4.1 on 2023-10-06 17:05

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [("auth", "0012_alter_user_first_name_max_length")]

    operations = [
        migrations.CreateModel(
            name="BloodType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("bloodType", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Tipo de sangre",
                "verbose_name_plural": "Tipos de sangre",
            },
        ),
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("phone_number", models.CharField(max_length=15)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        related_name="custom_users",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        related_name="custom_users",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={"verbose_name": "Usuario", "verbose_name_plural": "Usuarios"},
            managers=[("objects", django.contrib.auth.models.UserManager())],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity_beds", models.IntegerField()),
                ("room_number", models.IntegerField()),
            ],
            options={"verbose_name": "Ubicacion", "verbose_name_plural": "Ubicaciones"},
        ),
        migrations.CreateModel(
            name="SocialPlan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("socialPlan", models.CharField(max_length=255)),
            ],
            options={
                "verbose_name": "Plan social",
                "verbose_name_plural": "Planes sociales",
            },
        ),
        migrations.CreateModel(
            name="Doctor",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BackendApp.customuser",
                    ),
                ),
                ("specialty", models.CharField(max_length=255)),
            ],
            options={"verbose_name": "Doctor", "verbose_name_plural": "Doctores"},
            bases=("BackendApp.customuser",),
            managers=[("objects", django.contrib.auth.models.UserManager())],
        ),
        migrations.CreateModel(
            name="Calls",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("Normal", "Normal"), ("Emergencia", "Emergencia")],
                        default="Normal",
                        max_length=30,
                        verbose_name="Tipo",
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("Atendido", "Atendido"),
                            ("No atendido", "No atendido"),
                        ],
                        default="No atendido",
                        max_length=30,
                        verbose_name="Estado",
                    ),
                ),
                ("attendance_date", models.DateTimeField()),
                ("creation_date", models.DateTimeField()),
                (
                    "user_create_call",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="calls_created",
                        to="BackendApp.customuser",
                    ),
                ),
                (
                    "user_response_call",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="calls_responded",
                        to="BackendApp.customuser",
                    ),
                ),
            ],
            options={"verbose_name": "Llamada", "verbose_name_plural": "Llamadas"},
        ),
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "customuser_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="BackendApp.customuser",
                    ),
                ),
                ("height", models.FloatField()),
                ("weight", models.FloatField()),
                (
                    "bloodType",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="BackendApp.bloodtype",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="BackendApp.room",
                    ),
                ),
                (
                    "socialPlan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="BackendApp.socialplan",
                    ),
                ),
            ],
            options={"verbose_name": "Curso", "verbose_name_plural": "Cursos"},
            bases=("BackendApp.customuser",),
            managers=[("objects", django.contrib.auth.models.UserManager())],
        ),
    ]
