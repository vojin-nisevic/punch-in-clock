from django.views.generic import ListView
from core.models.user import Office


class Offices(ListView):
    model = Office
    template_name = 'office.html'
    Office.context_object_name = 'office_list'
    ordering = ['name']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Office.name
        return context
