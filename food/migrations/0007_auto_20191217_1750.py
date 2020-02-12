# Generated by Django 3.0 on 2019-12-17 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20191217_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='table',
        ),
        migrations.RemoveField(
            model_name='order',
            name='waiter',
        ),
        migrations.AddField(
            model_name='order',
            name='tableid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='table', to='food.Table'),
        ),
        migrations.AddField(
            model_name='order',
            name='waiterid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='order',
            name='isitopen',
            field=models.BooleanField(default=0),
        ),
    ]