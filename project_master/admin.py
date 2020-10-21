from django.contrib import admin

# Register your models here.

#from project_master.model import project_master_model
from project_master.models import *

admin.site.register(Project_Master)
admin.site.register(Tc_Details)


