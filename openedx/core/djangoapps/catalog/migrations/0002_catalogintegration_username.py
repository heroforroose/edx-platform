# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalogintegration',
            name='service_username',
            field=models.CharField(default=b'lms_catalog_service_user', help_text='Username created for Course Catalog Integration, e.g. lms_catalog_service_user.', max_length=100),
        ),
    ]
