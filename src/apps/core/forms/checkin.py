from django.forms import ModelForm, DateTimeField, TimeField
from django import forms
from django.conf import settings
from django.utils import timezone
from core.models.checkin import CheckInUser


class CheckInForm(ModelForm):
    employee_id = forms.IntegerField(required=False)
    punchin = DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS, initial=timezone.now().replace(microsecond=0), required=False)
    punchout = DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS, required=False)
    workhours = TimeField(required=False)

    def __init__(self, *args, **kwargs):
        super(CheckInForm, self).__init__(*args, **kwargs)
        [self.fields.pop(f) for f in self.fields.keys() if f in self.Meta.exclude]

    def clean_punchin(self):
        return timezone.now().replace(microsecond=0)

    class Meta:
        model = CheckInUser
        fields = ('employee_id', 'punchin', 'punchout', 'workhours')
        widgets = {'employee_id': forms.HiddenInput()}
        exclude = ('employee_id',)


class PunchOut(ModelForm):
    employee_id = forms.IntegerField(required=False)
    punchin = DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS, required=False)
    punchout = DateTimeField(input_formats=settings.DATETIME_INPUT_FORMATS, required=False)
    workhours = TimeField(required=False)

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

    def __init__(self, *args, **kwargs):
        super(PunchOut, self).__init__(*args, **kwargs)
        [self.fields.pop(f) for f in self.fields.keys() if f in self.Meta.exclude]
        for field in self:
            field.field.widget.attrs['readonly'] = True

    class Meta:
        model = CheckInUser
        fields = ('employee_id', 'punchin', 'punchout', 'workhours')
        exclude = ('employee_id',)
