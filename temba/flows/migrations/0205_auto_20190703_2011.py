# Generated by Django 2.1.8 on 2019-07-03 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("flows", "0204_flowstart_campaign_event")]

    operations = [
        migrations.AlterField(model_name="flow", name="flow_server_enabled", field=models.BooleanField(null=True))
    ]
