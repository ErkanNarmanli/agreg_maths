from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms
from agreg.settings import CREATE_USER_KEY
from .models import OPTION_CHOICES, Profil, current_year


class CreateUserForm(UserCreationForm):
    key = forms.CharField(
            label="Clée de sécurité",
            widget=forms.PasswordInput,
            help_text="Cette clée est fournie par l'administrateur"
                      " du site. Pour en obtenir une veuillez le"
                      " contacter."
            )
    year = forms.IntegerField(
                label="Année",
                validators=[MaxValueValidator(2042), MinValueValidator(2005)],
                help_text="Année pendant laquelle est passée le"
                          " concours. Par exemple en %d-%d mettre : %d"
                          % (current_year() - 1,
                             current_year(),
                             current_year()),
            )
    option = forms.ChoiceField(
            label='Option du concours',
            choices=OPTION_CHOICES,
            )
    error_m = {'wrong_key': "La clef fournie est eronnée."}
    initial = {'year': 2012}

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'year', 'option',
                  'password1', 'password2',)

    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        profil_year = self.cleaned_data["year"]
        profil_option = self.cleaned_data["option"]
        if commit:
            user.save()
            profil = Profil(user=user, year=profil_year, option=profil_option)
            profil.save()
        return user

    def clean_key(self):
        key = self.cleaned_data.get("key")
        if key != CREATE_USER_KEY:
            raise forms.ValidationError(
                    self.error_m['wrong_key'],
                    code='wrong_key')
        return key
