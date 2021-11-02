# Generated by Django 3.2.5 on 2021-09-05 17:30

import django.db.models.expressions
import django.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0115_alter_order_language_code"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                django.db.models.expressions.ExpressionWrapper(
                    models.Q(
                        (
                            "total_gross_amount__lt",
                            django.db.models.expressions.F("total_paid_amount"),
                        )
                    ),
                    output_field=django.db.models.fields.BooleanField,
                ),
                name="idx_overpaid",
            ),
        ),
        migrations.AddIndex(
            model_name="order",
            index=models.Index(
                django.db.models.expressions.ExpressionWrapper(
                    models.Q(
                        (
                            "total_gross_amount__lte",
                            django.db.models.expressions.F("total_paid_amount"),
                        )
                    ),
                    output_field=django.db.models.fields.BooleanField,
                ),
                name="idx_fully_paid",
            ),
        ),
    ]