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

]
