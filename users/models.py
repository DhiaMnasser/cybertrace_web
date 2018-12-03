from modelcluster.fields import ParentalKey
from django.db import models
from django.shortcuts import render
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.core.fields import RichTextField
from django.conf import settings
from django.core.serializers.json import DjangoJSONEncoder

from wagtailsurveys import models as surveys_models
from wagtailsurveys.models import AbstractFormSubmission
import json


class FormSubmission(AbstractFormSubmission):
    ip = models.GenericIPAddressField()

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.SET_NULL, null=True)

    def get_data(self):
        form_data = json.loads(self.form_data)
        form_data.update({
            'created_at': self.created_at,
            'user': self.user.username,
            'ip': self.ip
        })

        return form_data


class SurveyPage(surveys_models.AbstractSurvey):
    intro = RichTextField(blank=True)
    thank_you_text = RichTextField(blank=True)

    content_panels = surveys_models.AbstractSurvey.content_panels + [
        FieldPanel('intro', classname="full"),
        InlinePanel('survey_form_fields', label="Form fields"),
        FieldPanel('thank_you_text', classname="full"),
    ]

    def get_submission_class(self):
        return FormSubmission

    def process_form_submission(self, form, user, ip):
        obj = self.get_submission_class().objects.get(user=user)
        if obj:
            obj.delete()
        self.get_submission_class().objects.create(
            form_data=json.dumps(form.cleaned_data, cls=DjangoJSONEncoder),
            page=self,
            ip=ip, user=user,
        )

    def serve(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = self.get_form(request.POST, page=self, user=request.user)

            if form.is_valid():
                x_real_ip = request.META.get('HTTP_X_REAL_IP')
                if x_real_ip:
                    ip = x_real_ip
                else:
                    ip = request.META.get('REMOTE_ADDR')
                self.process_form_submission(form, request.user, ip)

                return render(
                    request,
                    self.landing_page_template,
                    self.get_context(request)
                )
        else:
            form = self.get_form(page=self, user=request.user)

        context = self.get_context(request)
        context['form'] = form
        return render(
            request,
            self.template,
            context
        )


class SurveyFormField(surveys_models.AbstractFormField):
    page = ParentalKey(SurveyPage, related_name='survey_form_fields')
