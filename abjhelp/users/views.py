"""Branches Views."""

# Django
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy

# Forms
from abjhelp.users.forms import HelpRequestForm, DonorRequestForm


class DashboardView(TemplateView):
    template_name = 'index.html'


class DisclaimerView(TemplateView):
    template_name = 'disclaimer.html'


class DisclaimerDonorView(TemplateView):
    template_name = 'disclaimer_donor.html'


class HelpRequestView(FormView):
    template_name = 'help_request.html'
    form_class = HelpRequestForm
    success_url = reverse_lazy('users:thanks')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class DonorRequestView(FormView):
    template_name = 'donor_request.html'
    form_class = DonorRequestForm
    success_url = reverse_lazy('users:thanks_donor')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ThanksView(TemplateView):
    template_name = 'thanks.html'


class ThanksDonorView(TemplateView):
    template_name = 'thank_donor.html'


class AdvisorView(TemplateView):
    template_name = 'legal_advisor.html'
