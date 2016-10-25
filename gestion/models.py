from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

OPTION_CHOICES = (
        ('A', 'Option A : Probabilités et statistiques'),
        ('B', 'Option B : Calcul scientifique'),
        ('C', 'Option C : Algèbre et calcul formel'),
        ('D', 'Option D : Modélisation et analyse de système informatique'),
    )

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    year = models.PositiveSmallIntegerField(
                validators=[MaxValueValidator(2042), MinValueValidator(2005)],
            )
    tex_preambule = models.TextField(
                "Préambule LaTeX personnalisé",
                blank = True,
            )
    option = models.CharField(
            'Option du concours',
            choices=OPTION_CHOICES,
            max_length=1,
            )

    class Meta:
        verbose_name = "profil agrégatif"
        verbose_name_plural = "profils agrégatifs"

    def __str__(self):
                return self.user.username

