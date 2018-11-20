# Generated by Django 2.0.8 on 2018-11-16 12:19

from datetime import timedelta

from django.db import migrations
from django.utils import timezone


def update_expiration(run):
    """
    Set our expiration according to the flow settings
    """
    if not run.flow.expires_after_minutes:
        return

    now = timezone.now()
    run.expires_on = run.modified_on + timedelta(minutes=run.flow.expires_after_minutes)

    # if it's in the past, just expire us now
    if run.expires_on < now:
        run.is_active = False
        run.exited_on = now
        run.exit_type = "E"
        run.child_context = None
        run.parent_context = None
        run.save(
            update_fields=[
                "expires_on",
                "is_active",
                "exited_on",
                "exit_type",
                "modified_on",
                "child_context",
                "parent_context",
            ]
        )
    else:
        # save our updated fields
        run.save(update_fields=["expires_on", "modified_on"])


def fix_ivr_and_ussd_runs_expiration_date(FlowRun):
    runs = FlowRun.objects.filter(is_active=True, expires_on=None).exclude(connection=None).select_related("flow")
    for run in runs:
        update_expiration(run)


def apply_migration(apps, schema_editor):
    FlowRun = apps.get_model("flows", "FlowRun")
    fix_ivr_and_ussd_runs_expiration_date(FlowRun)


def apply_manual():
    from temba.flows.models import FlowRun

    fix_ivr_and_ussd_runs_expiration_date(FlowRun)


class Migration(migrations.Migration):

    dependencies = [("flows", "0186_flow_session_indexes")]

    operations = [migrations.RunPython(apply_migration)]