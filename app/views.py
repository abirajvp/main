import jwt
from datetime import datetime, timedelta
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')


def view_call_logs(request):
    return render(request, 'call-logs.html')


def view_notifi_logs(request):
    return render(request, 'notifi-logs.html')


def view_text_logs(request):
    return render(request, 'text-logs.html')


def view_logs(request):
    return render(request, 'logs.html')


@csrf_exempt
def add_log(request):
    from app.models import Log, CallLog, TextLog, NotifiLog
    call_log = request.POST.get('call_log')
    notifi_log = request.POST.get('notifi_log')
    text_log = request.POST.get('text_log')
    log = request.POST.get('log')
    if call_log:
        logs = call_log.split('\n')
        for each_log in logs:
            CallLog.objects.create(log=each_log)
    if notifi_log:
        logs = notifi_log.split('\n')
        for each_log in logs:
            NotifiLog.objects.create(log=each_log)
    if text_log:
        logs = text_log.split('\n')
        for each_log in logs:
            TextLog.objects.create(log=each_log)
    if log:
        logs = log.split('\n')
        for each_log in logs:
            Log.objects.create(log=each_log)
    return JsonResponse({'status': 200, 'message': 'Log added'})


def fetch_logs(request):
    from app.models import Log
    from app.models import CallLog
    from app.models import NotifiLog
    from app.models import TextLog
    log_section = request.GET.get('log-section')
    if log_section == 'call':
        dblogs = CallLog.objects.all()
    elif log_section == 'notifi':
        dblogs = NotifiLog.objects.all()
    elif log_section == 'text':
        dblogs = TextLog.objects.all()
    else:
        dblogs = Log.objects.all()
    logs = []
    for log in dblogs:
        tim = str(log.created_at).split('.')[0]
        logs.append(log.log + ' - ' + tim)
    return JsonResponse({'status': 200, 'logs': logs})


def signup(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if not username or not email or not password:
        return JsonResponse({'status': 400, 'message': 'Missing parameters'})
    if User.objects.filter(Q(username=username) | Q(email=email)).exists():
        return JsonResponse({'status': 403, 'message': 'User already exists'})
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
    return JsonResponse({'status': 200, 'message': 'User created'})


def signin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'status': 200, 'message': 'User logged in'})
    return JsonResponse({'status': 403, 'message': 'Invalid credentials'})


def signout(request):
    logout(request)
    return JsonResponse({'status': 200, 'message': 'User logged out'})


def add_user(request):
    from app.models import UserData
    username = request.POST.get('username')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    password = request.POST.get('password')
    if not username or not email or not contact or not password:
        return JsonResponse({'status': 400, 'message': 'Missing parameters'})
    if UserData.objects.filter(Q(username=username) | Q(email=email) | Q(contact=contact)).exists():
        return JsonResponse({'status': 403, 'message': 'User already exists'})
    UserData.objects.create(username=username, email=email, contact=contact, password=password)
    return JsonResponse({'status': 200, 'message': 'User created'})


def get_user(request):
    from app.models import UserData
    username = request.GET.get('username')
    email = request.GET.get('email')
    contact = request.GET.get('contact')
    if not username and not email and not contact:
        return JsonResponse({'status': 400, 'message': 'Missing parameters'})
    user = UserData.objects.filter(Q(username=username) | Q(email=email) | Q(contact=contact)).first()
    if not user:
        return JsonResponse({'status': 404, 'message': 'User not found'})
    data = {'username': user.username, 'email': user.email, 'contact': user.contact, 'active': user.is_active, 'created_at': user.created_at, 'updated_at': user.updated_at}
    return JsonResponse({'status': 200, 'message': 'User found', 'data': data})


def update_user(request):
    from app.models import UserData
    username = request.POST.get('username')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    password = request.POST.get('password')
    if not username or not email or not contact or not password:
        return JsonResponse({'status': 400, 'message': 'Missing parameters'})
    user = UserData.objects.filter(Q(username=username) | Q(email=email) | Q(contact=contact)).first()
    if not user:
        return JsonResponse({'status': 404, 'message': 'User not found'})
    if username and username != user.username:
        user.username = username
    if email and email != user.email:
        user.email = email
    if contact and contact != user.contact:
        user.contact = contact
    if password:
        if password != user.password:
            user.password = password
        elif password == user.password:
            return JsonResponse({'status': 400, 'message': 'Password is same as before'})
    user.save()
    return JsonResponse({'status': 200, 'message': 'User updated'})

def delete_user(request):
    from app.models import UserData
    username = request.POST.get('username')
    email = request.POST.get('email')
    contact = request.POST.get('contact')
    if not username and not email and not contact:
        return JsonResponse({'status': 400, 'message': 'Missing parameters'})
    user = UserData.objects.filter(Q(username=username) | Q(email=email) | Q(contact=contact)).first()
    if not user:
        return JsonResponse({'status': 404, 'message': 'User not found'})
    user.delete()
    return JsonResponse({'status': 200, 'message': 'User deleted'})

def clear(request):
    from app.models import Log, CallLog, TextLog, NotifiLog
    Log.objects.all().delete()
    CallLog.objects.all().delete()
    TextLog.objects.all().delete()
    NotifiLog.objects.all().delete()
    return JsonResponse({'status': 200, 'message': 'Logs cleared'})