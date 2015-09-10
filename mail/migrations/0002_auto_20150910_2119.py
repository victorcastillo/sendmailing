# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox',
            name='response_mail_service',
            field=jsonfield.fields.JSONField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='inbox',
            name='tags',
            field=jsonfield.fields.JSONField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='inbox',
            name='to',
            field=jsonfield.fields.JSONField(max_length=500),
        ),
    ]
