# Generated by Django 5.0.3 on 2024-09-15 06:55

import django.db.models.expressions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_sale_profit'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='suggested_tip',
            field=models.GeneratedField(db_persist=True, expression=models.Case(models.When(income__gte=10, then=django.db.models.expressions.CombinedExpression(models.F('income'), '*', models.Value(0.2))), default=models.Value(0), output_field=models.DecimalField(decimal_places=2, max_digits=5)), output_field=models.DecimalField(decimal_places=2, max_digits=5)),
        ),
    ]
