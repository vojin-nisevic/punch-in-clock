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
from core.views.department import Departments
from core.views.department_create import DepartmentCreate
from core.views.department_UD import DepartmentUpdate
from core.views.department_delete import DepartmentDelete
from core.views.office import Offices
from core.views.office_create import OfficeCreate
from core.views.office_update import OfficeUpdate
from core.views.office_delete import OfficeDelete
from core.views.holiday import Holidays
from core.views.holiday_create import HolidayCreate
from core.views.holiday_update import HolidayUpdate
from core.views.holiday_delete import HolidayDelete
from core.views.freedays import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('core/', TemplateView.as_view(template_name='core/home.html'), name='home'),
    path('profile/<intLpk>/', Profile.as_view(template_name='core/profile.html'), name='profile'),
    path('base/', TemplateView.as_view(template_name='core/base.html'), name='base'),
    path('invite/', Invite.as_view(template_name='core/invite.html'), name='invite'),
    path('department/', Departments.as_view(template_name='core/department.html'), name='department'),
    path('department/add/', DepartmentCreate.as_view(template_name='core/department_create.html'),
         name='department-add'),
    path('department/update/<int:pk>', DepartmentUpdate.as_view(template_name='core/department_UD.html'),
         name='department-UD'),
    path('department/delete/<int:pk>/', DepartmentDelete.as_view(template_name='core/department_delete.html'),
         name='department-delete'),
    path('office/', Offices.as_view(template_name='core/office.html'), name='office'),
    path('office/add/', OfficeCreate.as_view(template_name='core/office_create.html'), name='office-add'),
    path('office/update/<int:pk>/', OfficeUpdate.as_view(template_name='core/office_update.html'),
         name='office-update'),
    path('office/delete/<int:pk>/', OfficeDelete.as_view(template_name='core/office_delete.html'),
         name='office-delete'),
    path('holiday/add/', HolidayCreate.as_view(template_name='core/holiday_create.html'),
         name='holiday-add'),
    path('holiday/', Holidays.as_view(template_name='core/holiday.html'), name='holiday'),
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
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

