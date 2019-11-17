from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
#from django.db.models.functions import Cast
from django.db.models import CharField
from django.db.models.fields import TimeField
from django.db.models.fields import DurationField
from django.db.models.fields import DateField
from django.utils.timezone import now
# Create your models here.

class User_Profile(models.Model):
    #user_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')
    friend_ID = models.ManyToManyField(User)
    #group_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')

class User_Group(models.Model):
    user_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')
    #Group_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')

class Event_user(models.Model):
    user_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')
    eventu_name = models.CharField(max_length = 50)
    eventu_startday = models.DateField(auto_now_add = False, null = False, default=datetime.now)
    eventu_starttime = models.TimeField( auto_now_add = False, null = False, default = '1')
    eventu_endday = models.DateField(auto_now_add = False, null = False, default=datetime.now)
    eventu_endtime = models.TimeField(auto_now_add = False, null = False, default = '1')
    eventu_location = models.CharField(max_length = 50, null = True)
    eventu_note = models.CharField(max_length=100, null = True)
    eventu_tag = models.CharField(max_length=25, null = True)
    #eventu_duration = models.DurationField (null = False)
    #eventu_starttime = models.DateTimeField(auto_now_add = False, null = False)
    #eventu_endtime = models.DateTimeField(auto_now_add = False, null = False)

    def __str__(self):
        statement = self.eventu_name
        if (self.eventu_startday == self.eventu_endday):
            statement += "~~ Day: " + str(self.eventu_startday) + " ~~ Time:" + str(self.eventu_starttime.hour) + ":"  
            statement += str(self.eventu_starttime.minute) + " - " + str(self.eventu_endtime.hour) + ":" + str(self.eventu_endtime.minute)
        else: 
            statement += "~~ Start Day and Time: " + str(self.eventu_startday) + " " + str(self.eventu_starttime.hour) + ":"  + str(self.eventu_starttime.minute)
            statement += "~~ End Day and Time: " + str(self.eventu_endday) + " " + str(self.eventu_endtime.hour) + ":" + str(self.eventu_endtime.minute)
        if (self.eventu_location != 'NA'):
            statement += " ~~ Location: " + self.eventu_location
        if (self.eventu_note != 'NA'):
            statement += " ~~ Notes: " + self.eventu_note
        if (self. eventu_tag != 'NA'):
            statement += " ~~ Tags: " + self.eventu_tag
        return statement

class Event_group(models.Model):
    #group_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')
    eventg_name = models.CharField(max_length = 50)
    eventg_startday = models.DateField(auto_now_add = False, null = False, default=datetime.now)
    eventg_starttime = models.TimeField( auto_now_add = False, null = False, default = '1')
    eventg_endday = models.DateField(auto_now_add = False, null = False, default=datetime.now)
    eventg_endtime = models.TimeField(auto_now_add = False, null = False, default = '1')
    eventg_location = models.CharField(max_length = 50, null = True)
    eventg_note = models.CharField(max_length=100, null = True)
    eventg_tag = models.CharField(max_length=25, null = True)
    def __str__(self):
        statement = self.eventg_name
        if (self.eventg_startday == self.eventg_endday):
            statement += "~~ Day: " + str(self.eventg_startday) + " ~~ Time:" + str(self.eventg_starttime.hour) + ":"  
            statement += str(self.eventg_starttime.minute) + " - " + str(self.eventg_endtime.hour) + ":" + str(self.eventg_endtime.minute)
        else: 
            statement += "~~ Start Day and Time: " + str(self.eventg_startday) + " " + str(self.eventg_starttime.hour) + ":"  + str(self.eventg_starttime.minute)
            statement += "~~ End Day and Time: " + str(self.eventg_endday) + " " + str(self.eventg_endtime.hour) + ":" + str(self.eventg_endtime.minute)
        if (self.eventg_location != 'NA'):
            statement += " ~~ Location: " + self.eventg_location
        if (self.eventg_note != 'NA'):
            statement += " ~~ Notes: " + self.eventg_note
        if (self. eventg_tag != 'NA'):
            statement += " ~~ Tags: " + self.eventg_tag
        return statement

class Task_user(models.Model):
    user_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')
    tasku_name = models.CharField(max_length = 50)
    tasku_duedate = models.DateTimeField(default=now, null = False)
    tasku_note = models.CharField(max_length=100, null = True, )
    tasku_tag = models.CharField(max_length=25, null = True)
    def __str__(self):
        statement = self.tasku_name
        statement += "~~ Due Day and Time: " + str(self.tasku_duedate.month) + " / " + str(self.tasku_duedate.day) + " "+ str(self.tasku_duedate.hour) + ":"  + str(self.tasku_duedate.minute)
        if (self.tasku_note != 'NA'):
            statement += " ~~ Notes: " + self.tasku_note
        if (self. tasku_tag != 'NA'):
            statement += " ~~ Tags: " + self.tasku_tag
        return statement

class Task_group(models.Model):
    #group_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')
    taskg_name = models.CharField(max_length = 50)
    taskg_duedate = models.DateTimeField(default=now, null = False)
    taskg_note = models.CharField(max_length=100, null = True)
    taskg_tag = models.CharField(max_length=25, null = True)
    def __str__(self):
        statement = self.taskg_name
        statement += " ~~ Due Day and Time: " + str(self.taskg_duedate.month) + " / " + str(self.taskg_duedate.day) + " "+ str(self.taskg_duedate.hour) + ":"  + str(self.taskg_duedate.minute)
        if (self.taskg_note != 'NA'):
            statement += " ~~ Notes: " + self.taskg_note
        if (self. taskg_tag != 'NA'):
            statement += " ~~ Tags: " + self.taskg_tag
        return statement
