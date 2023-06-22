from django.contrib import admin
from myApp.models import department,role,employee
# Register your models here.
admin.site.register(department)
admin.site.register(role)
admin.site.register(employee)