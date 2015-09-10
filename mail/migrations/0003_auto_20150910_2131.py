# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0002_auto_20150910_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbox',
            name='response_mail_service',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='inbox',
            name='tags',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='inbox',
            name='to',
            field=jsonfield.fields.JSONField(),
        ),
    ]
