"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf import settings
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from django.views.generic import TemplateView
from core.views.invite import Invite
from core.views.profile import Profile
from core.views.department import *
from core.views.office import *
from core.views.holiday import *
from core.views.freedays import *
from core.views.user import *
from core.views.vacations import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('core/', TemplateView.as_view(template_name='core/home.html'), name='home'),
    path('profile/<intLpk>/', Profile.as_view(template_name='core/profile.html'), name='profile'),
    path('base/', TemplateView.as_view(template_name='core/base.html'), name='base'),
    path('invite/', Invite.as_view(template_name='core/invite.html'), name='invite'),
    path('department/', Departmentslist.as_view(template_name='core/department.html'), name='department'),
    path('department/add/', DepartmentCreate.as_view(template_name='core/department_create.html'),
         name='department-add'),
    path('department/update/<int:pk>', DepartmentUpdate.as_view(template_name='core/department_UD.html'),
         name='department-UD'),
    path('department/delete/<int:pk>/', DepartmentDelete.as_view(template_name='core/department_delete.html'),
         name='department-delete'),
    path('office/', OfficesList.as_view(template_name='core/office.html'), name='office'),
    path('office/add/', OfficeCreate.as_view(template_name='core/office_create.html'), name='office-add'),
    path('office/update/<int:pk>/', OfficeUpdate.as_view(template_name='core/office_update.html'),
         name='office-update'),
    path('office/delete/<int:pk>/', OfficeDelete.as_view(template_name='core/office_delete.html'),
         name='office-delete'),
    path('holiday/add/', HolidayCreate.as_view(template_name='core/holiday_create.html'),
         name='holiday-add'),
    path('holiday/', HolidaysList.as_view(template_name='core/holiday.html'), name='holiday'),
    path('holiday/update/<int:pk>', HolidayUpdate.as_view(template_name='core/holiday_update.html'),
         name='holiday-update'),
    path('holiday/delete/<int:pk>', HolidayDelete.as_view(template_name='core/holiday_delete.html'),
         name='holiday-delete'),
    path('freedays/', FreeDaysList.as_view(template_name='core/freedays.html'), name='freedays'),
    path('freedays/add/', FreeDaysCreate.as_view(template_name='core/freedays_create.html'),
         name='freedays-add'),
    path('freedays/update/<int:pk>', FreeDaysUpdate.as_view(template_name='core/freedays_update.html'),
         name='freedays-update'),
    path('freedays/delete/<int:pk>', FreeDaysDelete.as_view(template_name='core/freedays_delete.htmpl'),
         name='freedays-delete'),
    path('user/register/', UserRegister.as_view(), name='user-register'),
    path('users/list/', UsersList.as_view(), name='users-list'),
    path('users/update/<int:pk>', UserUpdate.as_view(), name='user-update'),
    path('vacation/set/<int:pk>', VacationEmployeeCreate.as_view(), name='vacation-set'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

