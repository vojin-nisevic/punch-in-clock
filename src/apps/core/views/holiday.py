from django.views.generic import ListView
from core.models.holidays import Holidays


class Holidays(ListView):
    model = Holidays
    Holidays.context_object_name = 'holidays_list'

