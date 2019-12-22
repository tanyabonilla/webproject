from django import forms
from . import models
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


#class PostForm(forms.Form):
#    post = forms.CharField(label = 'Post', max_length = 240, validators = [validate_slug])

YEARSS= [x for x in range(2019,2022)]
#YEARSE= [x for x in range(2019,2020)]
TIME_INPUT_FORMATS = ['%I:%M %p',]

class Eventuser_Form(forms.Form):
    feventu_name = forms.CharField(label = 'Event Name', max_length = 50, required = True, strip = True)
    feventu_startday = forms.DateField(label = 'Start Day', required=True, widget = forms.SelectDateWidget(years = YEARSS))
    feventu_starttime = forms.TimeField(label = 'Start Time (HH:MM AM/PM)', required=True, input_formats = TIME_INPUT_FORMATS)
    feventu_endday = forms.DateField(label = 'End Day', required=True, widget = forms.SelectDateWidget(years = YEARSS))
    feventu_endtime = forms.TimeField(label = 'End Time (HH:MM AM/PM)',required=True, input_formats = TIME_INPUT_FORMATS)
    feventu_location = forms.CharField(label = 'Location', max_length = 50, required = False, strip = True, empty_value = 'NA')
    feventu_note = forms.CharField(label = 'Notes', max_length = 100, required = False, strip = True, empty_value = 'NA')
    feventu_tag = forms.CharField(label = 'Tags', max_length = 25, required = False, strip = True, empty_value = 'NA')
    #eventu_starttime = forms.DurationField(required=True)
    #feventu_starttime = forms.DateTimeField(label = 'Start Time', required=True, widget = forms.SplitDateTimeWidget(date_format = ['%m/%d/%y'], time_format = ['%I:%M']))
    #eventu_endtime = forms.DateTimeField(label = 'End Time',required=True, input_formats = ['%m/%d/%y %H:%M', '%m/%d/%y'])
    
    def save_eventu(self, request, commit=True):
        new_eventu = models.Event_user(eventu_name=self.cleaned_data['feventu_name'],
            user_ID = request.user,
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
    ftasku_name = forms.CharField(label = 'Task Name', max_length = 50, required = True, strip = True)
    #ftasku_duedate = forms.DateTimeField(label = 'Due Date and Time(mm/dd/yyyy h:m AM/PM))',required=True, input_formats = ('%m/%d/%Y %I:%M %A') ))
    ftasku_duedate = forms.DateTimeField(label = 'Due Date and Time(mm/dd/yyyy H:MM))',required=True,widget = forms.DateTimeInput())
    ftasku_note = forms.CharField(label = 'Notes', max_length = 100, required = False, strip = True, empty_value = 'NA')
    ftasku_tag = forms.CharField(label = 'Tags', max_length = 25, required = False, strip = True, empty_value = 'NA') 

    def save_tasku(self, request, commit=True):
        print("In save tasks")
        new_tasku = models.Task_user(tasku_name=self.cleaned_data['ftasku_name'],
            user_ID = request.user,
            tasku_duedate = self.cleaned_data['ftasku_duedate'],
            tasku_note = self.cleaned_data['ftasku_note'],
            tasku_tag = self.cleaned_data['ftasku_tag'],
            )
        if commit:
            new_tasku.save() #goes into the database
        return new_tasku

class Add_FriendForm(forms.Form):
    add_friend = forms.CharField(label = 'Name of the account you want to Befriend',  required = True, strip = True)

    def save_friend(self, request, commit=True):
        print("Form save_friend()")
        clean_friend = self.cleaned_data['add_friend']

        if(models.Friendship.objects.filter(user=request.user).exists()==False):
            create = models.Friendship(user=request.user)
            create.save()
        #checks if the friend you are trying to friend is a user
        if User.objects.filter(username=clean_friend).exists():
            user2 = User.objects.get(username=clean_friend)
            new_friend = models.FriendshipManager()
            #check if you are friends
            if(models.Friendship.objects.filter(user=user2).exists()==False):
                create2 = models.Friendship(user=user2)
                create2.save()
            if new_friend.befriend(request.user.id, user2):
                return new_friendship
        else:
            raise forms.ValidationError(u'Username "%s" does not exist.' % clean_friend)
       
class Remove_FriendForm(forms.Form):
    remove_friend = forms.CharField(label = 'Name of the account you want to Unfriend',  required = True, strip = True)

    def save_rfriend(self, request, commit=True):
        print("Form save_friend()")
        clean_friend = self.cleaned_data['remove_friend']

        if(models.Friendship.objects.filter(user=request.user).exists()==False):
            create = models.Friendship(user=request.user)
            create.save()
        #checks if the friend you are trying to unfriend is a user
        if User.objects.filter(username=clean_friend).exists():
            user2 = User.objects.get(username=clean_friend)
            new_friend = models.FriendshipManager()
            #check if you are friends
            if(models.Friendship.objects.filter(user=user2).exists()==False):
               raise forms.ValidationError(u'You are not friends with "%s" already.' % clean_friend)
            if new_friend.unfriend(request.user.id, user2):
                return new_friendship
        else:
            raise forms.ValidationError(u'Username "%s" does not exist.' % clean_friend)
       
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required=True)

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

    # def save_profile(self, user,commit = True):
    #     profile = models.User_Profile(user=user.pk)
    #     profile.save()

# class ChatForm(forms.Form):
#     chat = forms.CharField(label='Chatroom Name', max_length=25) 

#     def save(self, request, commit=True):
#         chat_instance = models.chatroom(
#             name = self.cleaned_data["chat"])

#         if commit:
#             chat_instance.save()
#         return chat_instance

