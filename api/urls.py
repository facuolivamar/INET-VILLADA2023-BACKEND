from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DoctorViewSet, CallsViewSet, PatientViewSet, RoomViewSet, BloodTypeViewSet, SocialPlanViewSet

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet)
router.register(r'calls', CallsViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'rooms', RoomViewSet)
router.register(r'bloodtypes', BloodTypeViewSet)
router.register(r'socialplans', SocialPlanViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Otras rutas específicas de la aplicación de la API si las tienes
]