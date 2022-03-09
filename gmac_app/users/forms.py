from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django import forms
from django.utils.translation import gettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(
        required=True,
        label=_("Full Name"),
        help_text=_("Your full name in the order you naturally write it."),
    )

    class Meta:
        model = get_user_model()
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    name = forms.CharField(
        required=True,
        label=_("Full Name"),
        help_text=_("Your full name in the order you naturally write it."),
    )

    class Meta:
        model = get_user_model()
        fields = ("email",)


class CustomUserEditForm(UserEditForm):
    name = forms.CharField(
        required=True,
        label=_("Full Name"),
        help_text=_("Your full name in the order you naturally write it."),
    )
    first_name = forms.CharField(required=True, label=_("Given Name"))
    last_name = forms.CharField(required=True, label=_("Family Name"))


class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(
        required=True,
        label=_("Full Name"),
        help_text=_("Your full name in the order you naturally write it."),
    )
    first_name = forms.CharField(required=True, label=_("Given Name"))
    last_name = forms.CharField(required=True, label=_("Family Name"))
