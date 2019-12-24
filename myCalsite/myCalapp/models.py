from django.db import models

from datetime import datetime
from django.contrib.auth.models import User
#from django.db.models.functions import Cast
from django.db.models import CharField
from django.db.models.fields import TimeField, DurationField, DateField, DateTimeField
from django.utils.timezone import now
from django.utils.translation import ugettext_lazy as _
# for userprofile
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class FriendshipManager(models.Manager):
    def befriend(self, user1, user2):
        print("In FriendshipManager befriend()")
        #curruser = User_Profile.objects.get(user = user1)
        friendship = Friendship.objects.get(user=user1)
        friendship.friends.add(Friendship.objects.get(user=user2))

    def unfriend(self, user1, user2):
        friendship = Friendship.objects.get(user=user1)
        friendship.friends.remove(Friendship.objects.get(user=user2))


class User_Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "profile", default = '1')
    bio = models.TextField(max_length=500, null=True, default = "")

    def __str__(self):
        return "%s user: %s id" % (self.user, self.user.id)
    
    #automatically makes a user profile
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            User_Profile.objects.create(user=instance)
    
    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    #group_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1'

class Friendship(models.Model):
    user = models.OneToOneField(User, related_name='curruser', on_delete = models.CASCADE, default = '1')
    friends = models.ManyToManyField('self', related_name = 'friended', symmetrical=False,  default = "1")

    def __str__(self):
        return "%s user" % (self.user)

    objects = FriendshipManager()

    def friend_count(self):
        return self.friends.count()
    friend_count.short_description = _(u'Friends count')
    def friend_summary(self, count=7):
        friend_list = self.friends.all().select_related(depth=1)[:count]
        return u'[%s%s]' % (u', '.join(unicode(f.user) for f in friend_list),
                            u', ...' if self.friend_count() > count else u'')
    friend_summary.short_description = _(u'Summary of friends')

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

class Task_user(models.Model):
    user_ID = models.ForeignKey(User, on_delete = models.CASCADE, default = '1')
    tasku_name = models.CharField(max_length = 50, null = False)
    tasku_duedate = models.DateField(default=now, null = False)
    tasku_note = models.CharField(max_length=100, null = True, )
    tasku_tag = models.CharField(max_length=25, null = True)
    def __str__(self):
        statement = self.tasku_name
        statement += "~~ Due Date: " + str(self.tasku_duedate.month) + " / " + str(self.tasku_duedate.day) 
        if (self.tasku_note != 'NA'):
            statement += " ~~ Notes: " + self.tasku_note
        if (self. tasku_tag != 'NA'):
            statement += " ~~ Tags: " + self.tasku_tag
        return statement

class Chatroom(models.Model):
    name = models.CharField(max_length=200, unique = True)
    
    def __str__(self):
        return self.name