from django.forms import ModelForm, Form
from .models import UserDetails

class SignInForm(ModelForm):
  class Meta:
    model = UserDetails