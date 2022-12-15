from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model
from django.forms import TextInput, CharField, PasswordInput

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

# TODO in the future move User Login Form here
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Username',
            'id': 'floatingInput'}
    ))
    password = CharField(widget=PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'floatingPassword',
        }
    ))