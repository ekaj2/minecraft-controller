from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET

# Create your views here.


def public_dashboard(request):
    return render(
        request, "public_dashboard.html",
        {
            'server_is_up': False,
        }
    )


def login_page(request):
    return render(
        request, "login_page.html",
        {
        }
    )


@login_required
@require_GET
def dashboard(request):
    return render(
        request, "dashboard.html",
        {
        }
    )
