# Generated by Django 3.0 on 2019-12-17 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.Order', unique=True),
        ),
        migrations.AlterField(
            model_name='check',
            name='percentage',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='food.ServicePercentage'),
        ),
    ]