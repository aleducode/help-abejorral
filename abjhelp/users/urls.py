from django.urls import path

from abjhelp.users import views as users_view
app_name = "users"
urlpatterns = [
    path(
        route="",
        view=users_view.DashboardView.as_view(),
        name='dashboard'
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
        route="donor",
        view=users_view.DonorRequestView.as_view(),
        name='donor'
    ),
    path(
        route="dis_donor",
        view=users_view.Dis_DonorView.as_view(),
        name='dis_donor'
    ),
    path(
        route="graciasD",
        view=users_view.Thanks_DonorView.as_view(),
        name='graciasD'
    ),

]
