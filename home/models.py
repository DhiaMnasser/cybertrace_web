from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page
from wagtail.contrib.forms.models import AbstractForm, AbstractFormField
from wagtail.admin.edit_handlers import (
    FieldPanel, FieldRowPanel,
    InlinePanel, MultiFieldPanel
)
from wagtail.core.fields import RichTextField
from wagtail.contrib.forms.edit_handlers import FormSubmissionsPanel


class HomePage(Page):
    pass


class FormField(AbstractFormField):
    page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')


class FormPage(AbstractForm):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = AbstractForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('intro', classname='full'),
        FieldPanel('thank_you_text', classname="full"),
        InlinePanel('form_fields', label="Form fields"),
    ]
