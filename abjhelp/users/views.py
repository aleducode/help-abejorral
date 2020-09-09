"""Branches Views."""

# Django
from django.views.generic import TemplateView, FormView, DetailView
from django.urls import reverse_lazy

# Forms
from abjhelp.users.forms import HelpRequestForm, DonorRequestForm
from abjhelp.users.models import HelpRequest


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

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ThanksView(TemplateView):
    template_name = 'thanks.html'


class ThanksDonorView(TemplateView):
    template_name = 'thank_donor.html'


class AdvisorView(TemplateView):
    template_name = 'legal_advisor.html'


class InformationView(TemplateView):
    template_name = 'information.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["helps"] = HelpRequest.objects.all()
        return context
    
class RequestDetailView(DetailView):
    template_name = 'detail.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    queryset = HelpRequest.objects.all()
    context_object_name = 'help'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        help_request = self.get_object()
        context["whatsapp"] = f'https://wa.me/57{help_request.phone_number}?text=Hola+{help_request.name},+te+escribo+por+el+pedido+que+hiciste+en+la+app+Un+Convite+por+Abejorral+https://unconviteporabejorral.org/detalle/{help_request.pk}'
        return context
    
