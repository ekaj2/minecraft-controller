from django.urls import path
from .views import public_dashboard, login_page, dashboard


urlpatterns = [
    path("", public_dashboard, name="public_dashboard"),
    path("login", login_page, name="login_page"),
    path("dashboard/", dashboard, name="dashboard"),
]
