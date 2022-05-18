# Generated by Django 3.2.13 on 2022-05-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0147_alter_orderevent_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="order",
            old_name="total_paid_amount",
            new_name="total_charged_amount",
        ),
        migrations.AddField(
            model_name="order",
            name="total_authorized_amount",
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12),
        ),
    ]
