# Generated by Django 4.1.3 on 2022-11-03 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_operation_slackusername"),
    ]

    operations = [
        migrations.AlterField(
            model_name="operation",
            name="slackUsername",
            field=models.CharField(default="maestro", max_length=20),
        ),
    ]
