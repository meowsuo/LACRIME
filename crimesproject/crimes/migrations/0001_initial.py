# Generated by Django 5.1.3 on 2024-12-05 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CrimeLookup",
            fields=[
                ("CrimeCode", models.IntegerField(primary_key=True, serialize=False)),
                ("CrimeCodeDescription", models.CharField(max_length=255)),
            ],
        ),
    ]
