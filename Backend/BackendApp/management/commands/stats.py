import random
from django.core.management.base import BaseCommand
from faker import Faker
from BackendApp.models import BloodType, SocialPlan, Room, CustomUser, Doctor, Calls, Patient
from django.contrib.auth import get_user_model

fake = Faker()

User = get_user_model()
class Command(BaseCommand):
    help = 'Carga de datos iniciales en la base de datos'

    def handle(self, *args, **options):
        
        # Generar datos para BloodType
        def generate_blood_types():
            for _ in range(10):
                BloodType.objects.create(bloodType=fake.word())

        # Generar datos para SocialPlan
        def generate_social_plans():
            for _ in range(10):
                SocialPlan.objects.create(socialPlan=fake.word())

        # Generar datos para Room
        def generate_rooms():
            for _ in range(10):
                Room.objects.create(
                    quantity_beds=random.randint(1, 10),
                    room_number=random.randint(101, 200)
                )

        # Generar datos para CustomUser (Usuarios)
        def generate_users():
            for _ in range(10):
                CustomUser.objects.create(
                    username=fake.user_name(),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    email=fake.email(),
                    phone_number=fake.phone_number()
                    # Agrega otros campos personalizados aquí si es necesario
                )

        # Generar datos para Doctor
        def generate_doctors():
            for _ in range(10):
                doctor = Doctor.objects.create(
                    username=fake.user_name(),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    email=fake.email(),
                    phone_number=fake.phone_number(),
                    specialty=fake.word()
                )
                # Asignar un grupo o permisos si es necesario
                # doctor.groups.add(grupo)
                # doctor.user_permissions.add(permiso)

        # Generar datos para Calls
        def generate_calls():
            users = CustomUser.objects.all()
            for _ in range(10):
                call = Calls.objects.create(
                    type=random.choice([c[0] for c in Calls.TypeComboBox.choices]),
                    state=random.choice([c[0] for c in Calls.StateComboBox.choices]),
                    attendance_date=fake.date_time_this_month(),
                    creation_date=fake.date_time_this_month(),
                    user_create_call=random.choice(users),
                    user_response_call=random.choice(users)
                )

        # Generar datos para Patient
        def generate_patients():
            rooms = Room.objects.all()
            blood_types = BloodType.objects.all()
            social_plans = SocialPlan.objects.all()
            for _ in range(10):
                Patient.objects.create(
                    room=random.choice(rooms),
                    bloodType=random.choice(blood_types),
                    socialPlan=random.choice(social_plans),
                    height=random.uniform(150, 200),
                    weight=random.uniform(50, 100),
                    username=fake.user_name(),
                    first_name=fake.first_name(),
                    last_name=fake.last_name(),
                    email=fake.email(),
                    phone_number=fake.phone_number()
                    # Agrega otros campos personalizados aquí si es necesario
                )

        if __name__ == "__main__":
            generate_blood_types()
            generate_social_plans()
            generate_rooms()
            generate_users()
            generate_doctors()
            generate_calls()
            generate_patients()

        self.stdout.write(self.style.SUCCESS("Guell hijo de puta"))
