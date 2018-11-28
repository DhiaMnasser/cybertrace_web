from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class EventIndexPage(Page):
    pass


class Event(Page):
    date = models.DateTimeField("Event date")
    intro = models.CharField("Event description", max_length=250, blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('intro'),
    ]

    def get_page_event_data(self):
        return {
            'type': 'page',
            'pk': self.pk,
            'author': str(self.owner),
            'description': self.intro,
            'status': self.status_string,
        }
