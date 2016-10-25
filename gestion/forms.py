from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from agreg.settings import CREATE_USER_KEY

class CreateUserForm(UserCreationForm):
    key             = forms.CharField(
            label="Clée de sécurité",
            widget=forms.PasswordInput,
            help_text="Cette clée est fournie par l'administrateur du site. Pour en obtenir une veuillez le contacter."
            )
    error_m  = { 'wrong_key': "La clef fournie est eronnée." }

    class Meta:
        model   = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user 

    def clean_key(self):
        key = self.cleaned_data.get("key")
        if key != CREATE_USER_KEY:
            raise forms.ValidationError(
                    self.error_m['wrong_key'],
                    code='wrong_key')
        return key

