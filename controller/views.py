from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.client('ec2', region_name='us-east-1')


def server_status_is(request, status="running"):
    server_is_up = False
    try:
        response = ec2.describe_instances(InstanceIds=['i-03beacf50b1544822'])
        print(response['Reservations'][0]['Instances'][0]['State']['Name'])
        server_is_up = response['Reservations'][0]['Instances'][0]['State']['Name'] == status
    except ClientError as e:
        print(e)
        return False
    return server_is_up


def server_status(request):

    return render(
        request, "status_dependent_management.html",
        {
            'server_is_running': server_status_is(request)
        }
    )


def public_dashboard(request):
    return render(request, "public_dashboard.html")


def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
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
    return render(request, "starting_server.html")


def starting_server(request):
    if server_status_is(request):
        # 286 to cancel htmx polling
        return HttpResponse("<h1>Server started successfully!</h1>", status=286)
    else:
        return HttpResponse("<h1>Starting server...</h1>")


def stopping_server(request):
    if server_status_is(request, "stopped"):
        # 286 to cancel htmx polling
        return HttpResponse("<h1>Server stopped successfully!</h1>", status=286)
    else:
        return HttpResponse("<h1>Stopping server...</h1>")


@login_required
@require_POST
def stop_server(request):
    ec2.stop_instances(InstanceIds=['i-03beacf50b1544822'])
    return render(request, "stopping_server.html")
