# Generated by Django 5.1.3 on 2024-11-27 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("services", "0002_remove_service_staff"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="service",
            name="applied_coupon_code",
        ),
    ]
