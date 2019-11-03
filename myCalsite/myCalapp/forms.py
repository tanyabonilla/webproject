from django import forms
from django.core.validators import validate_slug

#class PostForm(forms.Form):
#    post = forms.CharField(label = 'Post', max_length = 240, validators = [validate_slug])

YEARSS= [x for x in range(2019,2021)]
YEARSE= [x for x in range(2019,2021)]

class Eventuser_Form(forms.Form):
    feventu_name = forms.CharField(label = 'Event Name', max_length = 50, required = True, strip = True, validators = [validate_slug])
    #eventu_starttime = forms.DurationField(required=True)
    #eventu_starttime = forms.DateTimeField(label = 'Start Time', required=True, input_formats = ['%m/%d/%y %H:%M', '%m/%d/%y'])
    feventu_startday = forms.DateField(label = 'Start Day', required=True, widget = forms.SelectDateWidget(years = YEARSS))
    feventu_starttime = forms.TimeField(label = 'Start Time', required=True, widget = forms.TimeInput(format = '%H:%M'))
    feventu_endday = forms.DateField(label = 'End Day', required=True, widget = forms.SelectDateWidget(years = YEARSE))
    feventu_endtime = forms.TimeField(label = 'End Time',required=True, widget = forms.TimeInput(format = '%H:%M'))
    #eventu_endtime = forms.DateTimeField(label = 'End Time',required=True, input_formats = ['%m/%d/%y %H:%M', '%m/%d/%y'])
    feventu_location = forms.CharField(label = 'Location', max_length = 50, required = False, strip = True, empty_value = 'NA')
    feventu_note = forms.CharField(label = 'Notes', max_length = 100, required = False, strip = True, empty_value = 'NA')
    feventu_tag = forms.CharField(label = 'Tags', max_length = 25, required = False, strip = True, empty_value = 'NA')
    # eventu_duration = models.DurationFields()


# class EventForm(forms.Form):
#     Event_name = forms.CharField(label = 'Event Name', max_length=50, required=True, validators = [validate_slug])
#     time_start = forms.TimeField(label = 'Start time', required=False)
#     time_end = forms.TimeField(label = 'End time', required=False)
#     location = forms.CharField(label = 'Location', max_length=50, required=False)
#     WEEKDAY = (
#         ('Monday', 'Mon'),
#         ('Tuesday', 'Tues'),
#         ('Wednesday', 'Wed'),
#         ('Thursday', 'Thurs'),
#         ('Friday', 'Fri'),
#         ('Saturday', 'Sat'),
#         ('Sunday', 'Sun'),
#     )
#     weekday = forms.ChoiceField(choices=WEEKDAY)
