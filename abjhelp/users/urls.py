from django.urls import path

from abjhelp.users import views as users_view
app_name = "users"
urlpatterns = [
    path(
        route="",
        view=users_view.DashboardView.as_view(),
        name='index'
    ),
   	path(
        route="disclaimer",
        view=users_view.DisclaimerView.as_view(),
        name='disclaimer'
    ),

   	path(
        route="solicitud-ayuda",
        view=users_view.HelpRequestView.as_view(),
        name='help-request'
    ),
   	path(
        route="gracias😬",
        view=users_view.ThanksView.as_view(),
        name='thanks'
    ),
    path(
        route="advisor",
        view=users_view.AdvisorView.as_view(),
        name='advisor'
    ),
    path(
        route="donante",
        view=users_view.DonorRequestView.as_view(),
        name='donor'
    ),
    path(
        route="disclaimer_donante",
        view=users_view.DisclaimerDonorView.as_view(),
        name='dislcaimer_donor'
    ),
    path(
        route="gracias_donante",
        view=users_view.ThanksDonorView.as_view(),
        name='thanks_donor'
    ),

]
