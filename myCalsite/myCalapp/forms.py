from django import forms
from . import models
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#class PostForm(forms.Form):
#    post = forms.CharField(label = 'Post', max_length = 240, validators = [validate_slug])

YEARSS= [x for x in range(2019,2020)]
#YEARSE= [x for x in range(2019,2020)]
TIME_INPUT_FORMATS = ['%I:%M %p',]

class Eventuser_Form(forms.Form):
    feventu_name = forms.CharField(label = 'Event Name', max_length = 50, required = True, strip = True)
    feventu_startday = forms.DateField(label = 'Start Day', required=True, widget = forms.SelectDateWidget(years = YEARSS))
    feventu_starttime = forms.TimeField(label = 'Start Time (hh:mm AM/PM)', required=True, input_formats = TIME_INPUT_FORMATS)
    feventu_endday = forms.DateField(label = 'End Day', required=True, widget = forms.SelectDateWidget(years = YEARSS))
    feventu_endtime = forms.TimeField(label = 'End Time (hh:mm AM/PM)',required=True, input_formats = TIME_INPUT_FORMATS)
    feventu_location = forms.CharField(label = 'Location', max_length = 50, required = False, strip = True, empty_value = 'NA')
    feventu_note = forms.CharField(label = 'Notes', max_length = 100, required = False, strip = True, empty_value = 'NA')
    feventu_tag = forms.CharField(label = 'Tags', max_length = 25, required = False, strip = True, empty_value = 'NA')
    #eventu_starttime = forms.DurationField(required=True)
    #feventu_starttime = forms.DateTimeField(label = 'Start Time', required=True, widget = forms.SplitDateTimeWidget(date_format = ['%m/%d/%y'], time_format = ['%I:%M']))
    #eventu_endtime = forms.DateTimeField(label = 'End Time',required=True, input_formats = ['%m/%d/%y %H:%M', '%m/%d/%y'])
    
    def save_eventu(self, request, commit=True):
        new_eventu = models.Event_user(eventu_name = self.cleaned_data['feventu_name'],
            eventu_startday = self.cleaned_data['feventu_startday'],
            eventu_starttime = self.cleaned_data['feventu_starttime'],
            eventu_endday = self.cleaned_data['feventu_endday'],
            eventu_endtime = self.cleaned_data['feventu_endtime'],
            eventu_location = self.cleaned_data['feventu_location'],
            eventu_note = self.cleaned_data['feventu_note'],
            eventu_tag = self.cleaned_data['feventu_tag'],
            )
        if commit:
            print("saved eventu")
            new_eventu.save() #goes into the database
        return new_eventu
    
class Taskuser_Form(forms.Form):
    ftasku_name = forms.CharField(label = 'Event Name', max_length = 50, required = True, strip = True)
    ftasku_duedate = forms.DateTimeField(label = 'Due Date Time',required=True, input_formats = ('%m/%d/%Y %I:%M %p'))
    ftasku_note = forms.CharField(label = 'Notes', max_length = 100, required = False, strip = True, empty_value = 'NA')
    ftasku_tag = forms.CharField(label = 'Tags', max_length = 25, required = False, strip = True, empty_value = 'NA') 

    def save_tasku(self, request, commit=True):
        new_tasku = models.Task_user(eventu_name = form_instance_eu.cleaned_data['ftasku_name'],
            tasku_dudate = form_instance_eu.cleaned_data['ftasku_duedate'],
            tasku_note = form_instance_eu.cleaned_data['ftasku_note'],
            tasku_tag = form_instance_eu.cleaned_data['ftasku_tag'],
            )
        if commit:
            new_eventu.save() #goes into the database
        return new_eventu

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True
        )
        
    class Meta:
        model = User
        fields = ("username", "email",
                  "password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user