from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from bs4 import BeautifulSoup
from pypandoc import convert
from datetime import datetime

CATEGORY_CHOICES = (
        ('algebre', 'Algèbre et géométrie'),
        ('analyse', 'Analyse et probabilités'),
        ('informatique', 'Informatique'),
    )


def current_year():
    now = datetime.now()
    if now.month <= 7:
        return now.year
    else:
        return(now.year + 1)


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

    def __str__(self):
        return "%s, %d, %s" % (self.title,
                               self.year,
                               self.author)


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
    content = models.TextField(
            "Contenu du developpement",
            blank=True,
        )
    document = models.FileField(
            upload_to='dev/',
            blank=True,
        )

    class Meta:
        verbose_name = "développement"
        verbose_name_plural = "développements"

    def __str__(self):
        return self.title


class LessonTemplate(models.Model):
    num = models.PositiveSmallIntegerField(
            "Numéro de la leçon",
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
            help_text="Cocher la case si la leçon fait partie des"
                      " leçons sur lesquel peuvent être interrogés"
                      " les agrégation de l'option info. Cela concerne"
                      " donc toutes les leçons d'informatique  mais"
                      " aussi certaines leçons d'algèbre et d'analyse.",
        )
    jury = models.TextField(
            "Rapport du Jury",
            blank=True,
        )
    year = models.PositiveSmallIntegerField(
                "Année",
                default=current_year(),
                validators=[MaxValueValidator(2042), MinValueValidator(2005)],
                help_text="Année pendant laquelle est passée le concours."
                          " Par exemple en 2016-2017 mettre : 2017",
            )

    def has_effective(self, username):
        effectives = self.effective_lessons
        user = User.objects.get(username=username)
        liste = effectives.filter(author=user)
        return (liste.exists())

    def get_effective(self, username):
        effectives = self.effective_lessons
        user = User.objects.get(username=username)
        liste = effectives.filter(author=user)
        return liste.first()

    class Meta:
        verbose_name = "template de leçon"
        verbose_name_plural = "templates de leçons"

    def __str__(self):
        return "%d | %d | %s" % (self.year, self.num, self.title)


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
    references = models.ManyToManyField(
            Reference,
            related_name="lessons",
            # through="LessonReference",
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
        toc = soup.find(id="contentTOC")
        if toc is None:
            return ""
        else:
            return toc.prettify()

    class Meta:
        verbose_name = "leçon"
        verbose_name_plural = "leçons"

    def __str__(self):
        return "%s | %d | %s" % (self.author.username,
                                 self.template.num,
                                 self.template.title)

class EffectiveDevelopment(models.Model):
    development = models.ForeignKey(
            Development,
            related_name="effectiveUses",
            blank=True,
        )
    lessons = models.ManyToManyField(
            LessonTemplate,
            related_name="allDevs",
            help_text="Ajouter ici toutes les leçons auxquelles ce developpment"
                      " sera présenté.",
            blank=True,
            )
    user = models.ForeignKey(User)
    remarks = models.TextField("Remarques personnelles concernant"
                               " le développement.",
                               blank=True,)

    class Meta:
        verbose_name = "affectation de développement"
        verbose_name_plural = "affectation de développement"

    def __str__(self):
        return "%s -> %s " % (self.development.title,
                                  self.user.username,
                                  )

# class LessonReference(models.Models):
#     reference = models.ForeignKey(Reference)
#     lesson = models.ForeignKey(Lesson)
#     remarks = models.TextField("Remarques concernant la référence")
#
#     class Meta:
#         verbose_name = "référence pour une leçon"
#         verbose_name_plural = "références pour une leçon"
#
#     def __str__(self):
#         return "%s -> (%s | %d)" % (self.reference.title,
#                                     self.lesson.author.username,
#                                     self.lesson.template.num,
#                                     )
