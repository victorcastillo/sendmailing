# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0004_remove_inbox_error'),
    ]

    operations = [
        migrations.AddField(
            model_name='inbox',
            name='notified',
            field=models.BooleanField(default=False),
        ),
    ]
