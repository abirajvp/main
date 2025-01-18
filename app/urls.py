from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # auth related urls
    path('', views.index, name='index'),
    path('signup', csrf_exempt(views.signup), name='signup'),
    path('signin', csrf_exempt(views.signin), name='signin'),
    path('signout', csrf_exempt(views.signout), name='signout'),

    path('add-user', csrf_exempt(views.add_user), name='add_user'),
    path('get-user', csrf_exempt(views.get_user), name='get_user'),
    path('update-user', csrf_exempt(views.update_user), name='update_user'),
    path('delete-user', csrf_exempt(views.delete_user), name='delete_user'),

    # log operations
    path('add-log', csrf_exempt(views.add_log), name='add-log'),
    path('fetch-logs', views.fetch_logs, name='fetch-logs'),

    # view
    path('view-call-logs', views.view_call_logs, name='view-call-logs'),
    path('view-notifi-logs', views.view_notifi_logs, name='view-notifi-logs'),
    path('view-text-logs', views.view_text_logs, name='view-text-logs'),
    path('view-logs', views.view_logs, name='view-logs'),
    path('clear-abiraj', views.clear, name='clear'),
]
