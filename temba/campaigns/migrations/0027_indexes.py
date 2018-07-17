# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-07-16 16:59
from __future__ import unicode_literals

from django.db import migrations

SQL = """
CREATE INDEX IF NOT EXISTS campaigns_eventfire_fired_not_null_idx on campaigns_eventfire(fired) WHERE fired IS NOT NULL;
"""


class Migration(migrations.Migration):

    dependencies = [("campaigns", "0026_initial")]

    operations = [migrations.RunSQL(SQL)]