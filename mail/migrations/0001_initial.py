# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_mail_service', models.CharField(max_length=100)),
                ('error', models.TextField()),
                ('html', models.TextField()),
                ('subject', models.CharField(max_length=100)),
                ('from_email', models.EmailField(max_length=254)),
                ('from_name', models.CharField(max_length=100)),
                ('important', models.BooleanField(default=True)),
                ('track_opens', models.BooleanField(default=False)),
                ('track_clicks', models.BooleanField(default=False)),
                ('preserve_recipients', models.BooleanField(default=False)),
                ('tags', jsonfield.fields.JSONField()),
                ('to', jsonfield.fields.JSONField()),
                ('sent', models.BooleanField(default=False)),
                ('reject_reason', models.CharField(max_length=40, null=True)),
                ('id_mailing', models.TextField()),
                ('response_mail_service', jsonfield.fields.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_name', models.CharField(max_length=50)),
                ('service_url_extraction', models.URLField()),
                ('service_url_notification_id', models.URLField()),
                ('enabled', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='inbox',
            name='service',
            field=models.ForeignKey(to='mail.Service'),
        ),
    ]
