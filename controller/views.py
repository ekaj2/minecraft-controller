from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')


def public_dashboard(request):
    return render(
        request, "public_dashboard.html",
        {
            'server_is_up': False,
        }
    )


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/dashboard/')
    return render(
        request, "login_page.html",
        {
        }
    )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
@require_GET
def dashboard(request):
    return render(
        request, "dashboard.html",
        {
        }
    )


@login_required
@require_POST
def start_server(request):
    ec2.start_instances(InstanceIds=['i-03beacf50b1544822'])
    return HttpResponse("<h1>Starting server...</h1>")


@login_required
@require_POST
def stop_server(request):
    ec2.stop_instances(InstanceIds=['i-03beacf50b1544822'])
    return HttpResponse("<h1>Stopping server...</h1>")
