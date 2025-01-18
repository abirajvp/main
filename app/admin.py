from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(UserData)
admin.site.register(CallLog)
admin.site.register(NotifiLog)
admin.site.register(TextLog)
admin.site.register(Log)