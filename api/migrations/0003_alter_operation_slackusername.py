# Generated by Django 4.1.3 on 2022-11-03 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0002_alter_operation_result"),
    ]

    operations = [
        migrations.AlterField(
            model_name="operation",
            name="slackUsername",
            field=models.CharField(default="maestro", max_length=20, unique=True),
        ),
    ]