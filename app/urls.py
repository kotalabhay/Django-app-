from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include, re_path
#from app.views import registration,homepage
from app.views import registration, homepage , Dashboard
from project_master.views import *
from django.conf.urls.static import static
from Centermaster.views import *


#Authorization
urlpatterns = [
	path("", homepage.index, name="home"),
	path("register/", registration.register, name="register"),
	path("login/", registration.login_view, name="login"),
	path("logout/", registration.logout_view, name="logout"),
	re_path(r'^accounts/*', RedirectView.as_view(pattern_name='login', permanent=True)),
	path('unauthorized/', login_required(registration.UnAuthorized.as_view()), name = 'unauthorized'),

]


# Dashboard
urlpatterns += [
	path('dashboard/', never_cache(login_required(Dashboard.index)), name = 'dashboard'),
]

# Project Master
urlpatterns += [
	path('create_project/', never_cache(login_required(create_project)), name = 'create_project'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Center Master
urlpatterns += [
	path('create_center/', never_cache(login_required(create_center)), name = 'create_center'),
	path('center_master_insert/', never_cache(login_required(center_master_insert)), name ='center_master_insert'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


