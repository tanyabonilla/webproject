from django import forms
from django.core.validators import validate_slug

class PostForm(forms.Form):
    post = forms.CharField(label = 'Post', max_length = 240, validators = [validate_slug])

class Eventuser_Form(forms.Form):
    eventu_name = forms.CharField(label = 'Event Name', max_length = 50, required = True, strip = True, validators = [validate_slug])
    eventu_starttime = forms.DurationField(required=True)
    #eventu_starttime = forms.DateTimeField(required=True, input_formats = ['%m/%d/%y %H:%M', '%m/%d/%y'])
    #eventu_endtime = forms.DateTimeField(required=True, input_formats = ['%m/%d/%y %H:%M', '%m/%d/%y'])
    eventu_location = forms.CharField(label = 'Location', max_length = 50, required = False, strip = True, empty_value = 'NA')
    eventu_note = forms.CharField(label = 'Notes', max_length = 100, required = False, strip = True, empty_value = 'NA')
    eventu_tag = forms.CharField(label = 'tags', max_length = 25, required = False, strip = True, empty_value = 'NA')



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
