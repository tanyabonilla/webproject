from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
#from django.db.models.functions import Cast
from django.db.models import CharField
from django.db.models.fields import TimeField
from django.db.models.fields import DurationField
from django.db.models.fields import DateField
# Create your models here.

class User_Friends(models.Model):
    user_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')
    #friend_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')

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
    #eventu_duration = models.DurationField (null = False)
    #eventu_starttime = models.DateTimeField(auto_now_add = False, null = False)
    #eventu_endtime = models.DateTimeField(auto_now_add = False, null = False)
    eventu_location = models.CharField(max_length = 50, null = True)
    eventu_note = models.CharField(max_length=100, null = True)
    eventu_tag = models.CharField(max_length=25, null = True)

    def __str__(self):
        statement = self.eventu_name
        if (self.eventu_startday == self.eventu_endday):
            statement += "~~ Day: " + str(self.eventu_startday) + " ~~ Time:" + str(self.eventu_starttime.hour) + ":"  
            statement += str(self.eventu_starttime.minute) + " - " + str(self.eventu_endtime.hour) + ":" + str(self.eventu_endtime.minute)
        else: 
            statement += "~~ Start Day and Time: " + str(self.eventu_startday) + " " + str(self.eventu_starttime.hour) + ":"  + str(self.eventu_starttime.minute)
            statement += "~~ End Day and Time: " + str(self.eventu_endday) + " " + str(self.eventu_endtime.hour) + ":" + str(self.eventu_endtime.minute)
        if (self.eventu_location):
            statement += " ~~ Location: " + self.eventu_location
        if (self.eventu_note):
            statement += " ~~ Notes: " + self.eventu_note
        if (self. eventu_tag):
            statement += " ~~ Tags: " + self.eventu_tag
        return statement

class Event_group(models.Model):
    #group_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')
    eventg_name = models.CharField(max_length = 50)
    eventg_starttime = models.DateTimeField(auto_now_add = False, null = False)
    eventg_endtime = models.DateTimeField(auto_now_add = False, null = False)
    eventg_location = models.CharField(max_length = 50, null = True)
    eventg_note = models.CharField(max_length=100, null = True)
    eventg_tag = models.CharField(max_length=25, null = True)

class Task_user(models.Model):
    user_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')
    tasku_name = models.CharField(max_length = 50)
    tasku_duedate = models.DateTimeField(auto_now_add = True, null = True)
    tasku_note = models.CharField(max_length=100, null = True)
    tasku_tag = models.CharField(max_length=25, null = True)

class Task_group(models.Model):
    #user_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')
    taskg_name = models.CharField(max_length = 50)
    taskg_duedate = models.DateTimeField(auto_now_add = True, null = True)
    taskg_note = models.CharField(max_length=100, null = True)
    taskg_tag = models.CharField(max_length=25, null = True)
    

    # def __str__(self):
    #     if (self.time_start and self.time_end and self.location):
    #         return (self.Event_name + "------\n\nLocation: " + self.location + ", \nWeekday: "+ self.weekday +
    #         ", \nTime: "+ str(self.time_start)+ " - " + str(self.time_end))
    #     elif (self.time_start is None and self.time_end is None and self.location):
    #         return (self.Event_name + "------\n\nLocation: " + self.location + ", \nWeekday: "+ self.weekday)
    #     else:
    #         return self.Event_name    

    #def event_string(self):
    #    if (self.time_start and self.time_end and self.location):
    #        return self.Event_name + "\nLocation: " + self.location + "\nWeekday: "+ self.weekday +"\nTime: "+ self.time_start+ " - " + self.time_end

