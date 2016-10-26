from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
from django.core.urlresolvers import reverse_lazy
from pypandoc import convert

register = template.Library()

@register.filter
@stringfilter
def pandoc(text, level="1"):
    return mark_safe(convert(
                        text,
                        'html',
                        format='md',
                        extra_args=['--mathjax',
                                    '--base-header-level='+level,
                                    ],
                    ))


@register.filter
@stringfilter
def content_pandoc(text, level="1"):
    return mark_safe(convert(
                        text,
                        'html',
                        format='md',
                        extra_args=['--mathjax',
                                    '--base-header-level='+level,
                                    '--number-sections',
                                    # '--toc',
                                    # '--toc-depth=6',
                                    '--id-prefix=content',
                                    # '-s',
                                    ],
                    ))

@register.simple_tag
def is_started_class(lesson, user):
    effectives = lesson.effective_lessons
    liste = effectives.filter(author=user)
    if liste.exists():
        return mark_safe("started")
    else:
        return mark_safe("not-yet")

@register.simple_tag
def href_open_or_not(lesson, user):
    effectives = lesson.effective_lessons
    liste = effectives.filter(author=user)
    if liste.exists():
        return mark_safe(
                """<a href="%s">""" % reverse_lazy('oral:detail', args=(user.username, lesson.num))
                )
    else:
        return ""

@register.simple_tag
def href_close_or_not(lesson, user):
    effectives = lesson.effective_lessons
    liste = effectives.filter(author=user)
    if liste.exists():
        return mark_safe("</a>")
    else:
        return ""
