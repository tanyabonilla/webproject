from django import forms
from django.core.validators import validate_slug

#class PostForm(forms.Form):
#    post = forms.CharField(label = 'Post', max_length = 240, validators = [validate_slug])

YEARSS= [x for x in range(2019,2021)]
YEARSE= [x for x in range(2019,2021)]

class Eventuser_Form(forms.Form):
    feventu_name = forms.CharField(label = 'Event Name', max_length = 50, required = True, strip = True, validators = [validate_slug])
    feventu_startday = forms.DateField(label = 'Start Day', required=True, widget = forms.SelectDateWidget(years = YEARSS))
    feventu_starttime = forms.TimeField(label = 'Start Time', required=True,  input_formats = ('%I:%M %p'))
    feventu_endday = forms.DateField(label = 'End Day', required=True, widget = forms.SelectDateWidget(years = YEARSE))
    feventu_endtime = forms.TimeField(label = 'End Time',required=True, input_formats = ('%I:%M %p'))
    feventu_location = forms.CharField(label = 'Location', max_length = 50, required = False, strip = True, empty_value = 'NA')
    feventu_note = forms.CharField(label = 'Notes', max_length = 100, required = False, strip = True, empty_value = 'NA')
    feventu_tag = forms.CharField(label = 'Tags', max_length = 25, required = False, strip = True, empty_value = 'NA')
    #eventu_starttime = forms.DurationField(required=True)
    #feventu_starttime = forms.DateTimeField(label = 'Start Time', required=True, widget = forms.SplitDateTimeWidget(date_format = ['%m/%d/%y'], time_format = ['%I:%M']))
    #eventu_endtime = forms.DateTimeField(label = 'End Time',required=True, input_formats = ['%m/%d/%y %H:%M', '%m/%d/%y'])