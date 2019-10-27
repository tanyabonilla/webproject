from django import forms
from django.core.validators import validate_slug

class PostForm(forms.Form):
    post = forms.CharField(label = 'Post', max_length = 240, validators = [validate_slug])

class EventForm(forms.Form):
    Event_name = forms.CharField(label = 'Event Name', max_length=50, required=True, validators = [validate_slug])
    time_start = forms.TimeField(label = 'Start time', required=False)
    time_end = forms.TimeField(label = 'End time', required=False)
    location = forms.CharField(label = 'Location', max_length=50, required=False)
    WEEKDAY = (
        ('Monday', 'Mon'),
        ('Tuesday', 'Tues'),
        ('Wednesday', 'Wed'),
        ('Thursday', 'Thurs'),
        ('Friday', 'Fri'),
        ('Saturday', 'Sat'),
        ('Sunday', 'Sun'),
    )
    weekday = forms.ChoiceField(choices=WEEKDAY)
