from django.urls import path
from .views import public_dashboard, login_page, dashboard, start_server, stop_server, logout_view


urlpatterns = [
    path("", public_dashboard, name="public_dashboard"),
    path("login/", login_page, name="login_page"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard, name="dashboard"),
    path("start-server/", start_server, name="start-server"),
    path("stop-server/", stop_server, name="stop-server"),
]
