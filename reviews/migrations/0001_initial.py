# Generated by Django 4.1.2 on 2022-10-11 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("movies", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("stars", models.IntegerField()),
                ("review", models.TextField()),
                ("spoilers", models.BooleanField(default=False)),
                (
                    "recomendation",
                    models.CharField(
                        choices=[
                            ("Must Watch", "Must"),
                            ("Should Watch", "Should"),
                            ("Avoid Watch", "Avoid"),
                            ("No Opinion", "Default"),
                        ],
                        default="No Opinion",
                        max_length=50,
                    ),
                ),
                (
                    "movies",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="movies.movie",
                    ),
                ),
            ],
        ),
    ]