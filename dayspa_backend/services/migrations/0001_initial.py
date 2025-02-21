# Generated by Django 5.1.3 on 2024-11-21 11:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Coupon",
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
                ("coupon_code", models.CharField(max_length=50, unique=True)),
                ("discount", models.DecimalField(decimal_places=2, max_digits=5)),
                ("valid_from", models.DateTimeField()),
                ("valid_until", models.DateTimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("service_name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                ("duration", models.IntegerField(help_text="Duration in minutes")),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "service_image",
                    models.ImageField(blank=True, null=True, upload_to="services/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "applied_coupon_code",
                    models.CharField(
                        blank=True,
                        help_text="Coupon code entered by user for this service",
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "coupon",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="services.coupon",
                    ),
                ),
                (
                    "staff",
                    models.ForeignKey(
                        limit_choices_to=models.Q(
                            ("user_role__role_name", "Customer"), _negated=True
                        ),
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="services",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="StaffService",
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
                ("is_primary", models.BooleanField(default=False)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="services.service",
                    ),
                ),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("staff", "service")},
            },
        ),
    ]
