"""Branches Views."""

# Django
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

# Forms
from abjhelp.users.forms import HelpRequestForm


class DashboardView(TemplateView):
    template_name = 'index.html'


class DisclaimerView(TemplateView):
    template_name = 'disclaimer.html'


class HelpRequestView(FormView):
    template_name = 'help_request.html'
    form_class = HelpRequestForm
    success_url = reverse_lazy('users:thanks')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ThanksView(TemplateView):
    template_name = 'thanks.html'


class AdvisorView(TemplateView):
    template_name = 'legal_advisor.html'
