from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView

from wagtail.documents.models import Document


class RulesView(TemplateView):
    template_name = 'users/rules_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['file'] = Document.objects.filter(title='reglement.pdf').\
            first()
        return context


class VotesView(TemplateView):
    template_name = 'users/rules_view.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['file'] = Document.objects.filter(title='reglement.pdf').\
            first()
        return context
