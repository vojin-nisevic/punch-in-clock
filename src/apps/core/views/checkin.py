from django.views.generic import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse_lazy, reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from core.models.checkin import *
from core.forms.checkin import *


class CheckInCreate(SuccessMessageMixin, CreateView):
    model = CheckInUser
    form_class = CheckInForm
    success_url = reverse_lazy('home')
    success_message = _('You have successfully checked in')
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        if CheckInUser.objects.filter(employee_id=request.user.id, punchin__isnull=False, punchout__isnull=True).exists():
            return HttpResponseRedirect(reverse('punchout'))
        else:
            form = self.form_class(None)
            return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        ciu = CheckInUser(employee_id=self.request.user.id, punchin=timezone.now().replace(microsecond=0))
        ciu.save()
        return HttpResponseRedirect(reverse('punchout'))


class CheckOut(SuccessMessageMixin, UpdateView):
    # ccid = 0
    model = CheckInUser
    form_class = PunchOut
    success_url = reverse_lazy('logout')
    template_name = 'core/punchout.html'
    # success_message = _('')

    def format_timedelta(i, td):
        hours, remainder = divmod(td, 3600)
        minutes, seconds = divmod(remainder, 60)
        hours, minutes, seconds = int(hours), int(minutes), int(seconds)
        if hours < 10:
            hours = '0%s' % int(hours)
        if minutes < 10:
            minutes = '0%s' % minutes
        if seconds < 10:
            seconds = '0%s' % seconds
        return '%s:%s:%s' % (hours, minutes, seconds)

    def get_object(self, queryset=None):
        obj = CheckInUser.objects.filter(employee_id=self.request.user.id, punchin__isnull=False, punchout__isnull=True).first()
        return obj

    def form_valid(self, form):
        form.instance.punchout = timezone.now().replace(microsecond=0)
        wh = (timezone.now().replace(microsecond=0) - form.instance.punchin).total_seconds()
        whr = self.format_timedelta(wh)
        form.instance.workhours = whr
        self.success_message = _('You have worked for ' + whr[-1:2] + ' hours')
        return super().form_valid(form)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(self.request.POST)
    #     # import ipdb
    #     # ipdb.set_trace()
    #     if form.is_valid():
    #         check = form.save(commit=False)
    #         # cid = CheckInUser.__getattribute__(CheckInUser, 'pk')
    #         # import ipdb
    #         # ipdb.set_trace()
    #         form.instance.employee_id = self.ccid
    #         import ipdb
    #         ipdb.set_trace()
    #         check.id = self.ccid
    #         check.employee_id = self.request.user.id
    #         check.punchin = form.cleaned_data['punchin']
    #         check.punchout = timezone.now().replace(microsecond=0)
    #         cin = form.cleaned_data['punchin']
    #         cout = timezone.now().replace(microsecond=0)
    #         wraw = (cout - cin).total_seconds()
    #         wh = self.format_timedelta(wraw)
    #         check.workhours = wh
    #         # import ipdb
    #         # ipdb.set_trace()
    #         check.save()
    #         return HttpResponseRedirect(reverse('logout'))
    #         # return render(request, self.template_name, {'form': form})
    #     else:
    #         pun = form.save(commit=False)
    #         pun.employee_id = self.request.user.id
    #         pun.punchin = self.request
    #     us = ''
    #     for cor, val in self.request.content_params:
    #         us += val
    #     us = self.request.content_params
    #     import ipdb
    #     ipdb.set_trace()
    #     return HttpResponse('majmune' + ' ' + us)
        # import ipdb
        # ipdb.set_trace()

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(self.request.POST)
    #     check = form.save(commit=False)
    #     check.employee_id = self.request.user.id
    #     cout = timezone.now().replace(microsecond=0)
    #     check.punchout = cout
    #     cin = form.cleaned_data['punchin']
    #     whraw = (cout - cin).total_seconds()
    #     wh = CheckOut.format_timedelta(whraw)
    #     check.workhours = wh
    #     check.save()
    #     return render(request, self.template_name, {'form': form})
