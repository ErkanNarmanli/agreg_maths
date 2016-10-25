from django.contrib.auth.models import User
from django.db import models
from bs4 import BeautifulSoup
from pypandoc import convert

CATEGORY_CHOICES = (
        ('algebre', 'Algèbre et géométrie'),
        ('analyse', 'Analyse et probabilités'),
        ('informatique', 'Informatique'),
    )

class Reference(models.Model):
    title = models.CharField(
            "Titre",
            max_length=200,
        )
    slug = models.SlugField(
            "Identificateur",
            unique=True,
            primary_key=True,
        )
    author = models.CharField(
            "Auteur",
            max_length=200,
        )
    year = models.PositiveSmallIntegerField(
            "Année de publication",
            blank=True,
        )
    document = models.FileField(
            upload_to='ref/',
            blank=True,
        )
    description = models.TextField(
            "Description",
            blank=True,
        )

    class Meta:
        verbose_name = "référence"
        verbose_name_plural = "références"


class Development(models.Model):
    title = models.CharField(
            "Titre",
            max_length=200,
        )
    references = models.ManyToManyField(
            Reference,
            related_name="developments",
            blank=True,
        )

    class Meta:
        verbose_name = "développement"
        verbose_name_plural = "développements"


class LessonTemplate(models.Model):
    num = models.PositiveSmallIntegerField(
            "Numéro de la leçon",
            unique_for_year=True,
        )
    title = models.CharField(
            "Nom de la leçon",
            max_length=200,
        )
    category = models.CharField(
            "Catégorie",
            choices=CATEGORY_CHOICES,
            max_length=200,
        )
    is_for_info = models.BooleanField(
            "Pour option info",
            help_text="Cocher la case si la leçon fait partie des leçons"
                      " sur lesquel peuvent être interrogés les agrégation de l'option info."
                      " Cela concerne donc toutes les leçons d'informatique mais aussi certaines"
                      " leçons d'algèbre et d'analyse.",
        )
    jury = models.TextField(
            "Rapport du Jury",
            blank=True,
        )


class Lesson(models.Model):
    template = models.ForeignKey(
            LessonTemplate,
            related_name="effective_lessons",
        )
    author = models.ForeignKey(
            User,
            related_name="lessons",
        )
    content = models.TextField(
            "Contenu de la leçon",
            blank=True,
        )
    remarks = models.TextField(
            "Mes remarques",
            blank=True,
        )
    developments = models.ManyToManyField(
            Development,
            related_name="lessons",
            blank=True,
        )
    references = models.ManyToManyField(
            Reference,
            related_name="lessons",
            blank=True,
        )
    is_finished = models.BooleanField("Leçon terminée")

    def get_toc(self):
        html = convert(
                    self.content,
                    'html',
                    format='md',
                    extra_args=['--mathjax',
                                # '--base-header-level='+level,
                                '--number-sections',
                                '--toc',
                                '--toc-depth=6',
                                '--id-prefix=content',
                                '-s',
                                ],
                )
        soup = BeautifulSoup(html, "lxml")
        return soup.find(id="contentTOC").prettify()

    class Meta:
        verbose_name = "leçon"
        verbose_name_plural = "leçons"
