from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class CustomUserChangeForm(forms.ModelForm):
    current_password = forms.CharField(widget=forms.PasswordInput, label='Senha Atual')

    class Meta:
        model = CustomUser
        fields = ['username', 'email']

    def clean_current_password(self):
        current_password = self.cleaned_data['current_password']
        if not self.instance.check_password(current_password):
            raise forms.ValidationError('A senha atual está incorreta.')
        return current_password
