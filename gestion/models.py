from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    year = models.PositiveSmallIntegerField(
                validators=[MaxValueValidator(2042), MinValueValidator(2005)],
            )
    tex_preambule = models.TextField(
                "Préambule LaTeX personnalisé",
                blank = True,
            )

    class Meta:
        verbose_name = "profil agrégatif"
        verbose_name_plural = "profils agrégatifs"

    def __str__(self):
                return self.user.username

