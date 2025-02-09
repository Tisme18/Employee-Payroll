# Generated by Django 5.0.1 on 2024-05-10 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payroll_app', '0002_alter_employee_allowance_alter_employee_overtime_pay_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='overtime_pay',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='rate',
            field=models.FloatField(null=True),
        ),
    ]
