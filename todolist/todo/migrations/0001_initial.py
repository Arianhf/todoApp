# Generated by Django 2.2 on 2019-04-25 14:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a group name', max_length=100, verbose_name='name')),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
            },
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='a title for your to-do item', max_length=250, verbose_name='title')),
                ('description', models.TextField(blank=True, help_text='a description for to-do item', verbose_name='description')),
                ('created', models.DateField(blank=True, default=django.utils.timezone.now, help_text='creation date of to-do item', verbose_name='created')),
                ('status', models.CharField(blank=True, choices=[('p', 'Pending'), ('d', 'Done')], default='p', help_text='to-do item status', max_length=1, verbose_name='status')),
                ('group', models.ForeignKey(blank=True, default='general', help_text='group of to-do item', null=True, on_delete=django.db.models.deletion.SET_NULL, to='todo.Group', verbose_name='group')),
                ('user', models.ForeignKey(help_text='user that the to-do items belongs to', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
