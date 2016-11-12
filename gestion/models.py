from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime

OPTION_CHOICES = (
        ('A', 'Option A : Probabilités et statistiques'),
        ('B', 'Option B : Calcul scientifique'),
        ('C', 'Option C : Algèbre et calcul formel'),
        ('D', 'Option D : Modélisation et analyse de système informatique'),
    )


def current_year():
    now = datetime.now()
    if now.month <= 7:
        return now.year
    else:
        return(now.year + 1)


class Profil(models.Model):
    user = models.OneToOneField(User, related_name="profil")
    year = models.PositiveSmallIntegerField(
                "Année",
                default=current_year(),
                validators=[MaxValueValidator(2042), MinValueValidator(2005)],
                help_text="Année pendant laquelle est passée le concours."
                          " Par exemple en 2016-2017 mettre : 2017",
            )
    tex_preambule = models.TextField(
                "Préambule LaTeX personnalisé",
                blank=True,
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
