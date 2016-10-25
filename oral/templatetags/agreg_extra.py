from django import template
from django.utils.safestring import mark_safe
from django.template.defaultfilters import stringfilter
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
