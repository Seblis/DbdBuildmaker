from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import BuildmakerUserCreationForm, BuildmakerUserChangeForm

BuildmakerUser = get_user_model()


class BuildmakerUserAdmin(UserAdmin):
    add_form = BuildmakerUserCreationForm
    form = BuildmakerUserChangeForm
    model = BuildmakerUser
    list_display = [
        'email',
        'username',
        'is_superuser',
    ]


admin.site.register(BuildmakerUser, BuildmakerUserAdmin)
