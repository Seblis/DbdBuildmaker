from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class BuildmakerUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
        )


class BuildmakerUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'email',
        )