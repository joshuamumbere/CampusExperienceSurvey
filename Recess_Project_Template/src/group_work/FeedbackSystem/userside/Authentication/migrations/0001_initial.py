# Generated by Django 4.2.4 on 2023-08-08 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("student_number", models.CharField(max_length=10, unique=True)),
                (
                    "year",
                    models.CharField(
                        choices=[
                            ("One", "Year One"),
                            ("Two", "Year Two"),
                            ("Three", "Year Three"),
                            ("Four", "Year Four"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]
