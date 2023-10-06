from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import (UserAccount,)


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = "__all__"