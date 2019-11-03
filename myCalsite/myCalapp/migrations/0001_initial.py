# Generated by Django 2.2.5 on 2019-11-03 20:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventg_name', models.CharField(max_length=50)),
                ('eventg_starttime', models.DateTimeField()),
                ('eventg_endtime', models.DateTimeField()),
                ('eventg_location', models.CharField(max_length=50, null=True)),
                ('eventg_note', models.CharField(max_length=100, null=True)),
                ('eventg_tag', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task_group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskg_name', models.CharField(max_length=50)),
                ('taskg_duedate', models.DateTimeField(auto_now_add=True, null=True)),
                ('taskg_note', models.CharField(max_length=100, null=True)),
                ('taskg_tag', models.CharField(max_length=25, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ID', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='User_Friends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_ID', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tasku_name', models.CharField(max_length=50)),
                ('tasku_duedate', models.DateTimeField(auto_now_add=True, null=True)),
                ('tasku_note', models.CharField(max_length=100, null=True)),
                ('tasku_tag', models.CharField(max_length=25, null=True)),
                ('user_ID', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventu_name', models.CharField(max_length=50)),
                ('eventu_startday', models.DateField(default=datetime.datetime.now)),
                ('eventu_starttime', models.TimeField(default='1')),
                ('eventu_endday', models.DateField(default=datetime.datetime.now)),
                ('eventu_endtime', models.TimeField(default='1')),
                ('eventu_location', models.CharField(max_length=50, null=True)),
                ('eventu_note', models.CharField(max_length=100, null=True)),
                ('eventu_tag', models.CharField(max_length=25, null=True)),
                ('user_ID', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]