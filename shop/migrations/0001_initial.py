# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bicycle',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('model', models.CharField(max_length=200)),
                ('marca', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
                ('imagen', models.ImageField(max_length=200, upload_to='img', default='img/bici.png')),
                ('video', models.FileField(max_length=200, upload_to='vid', default='vid/sample.mp4')),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
