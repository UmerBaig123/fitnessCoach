# Generated by Django 4.2.13 on 2024-08-01 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_log_log_foods'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='log_foods',
            name='calories',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='log_foods',
            name='carbs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='log_foods',
            name='fat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='log_foods',
            name='portion',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='log_foods',
            name='protein',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_foods',
            name='calories',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_foods',
            name='carbs',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_foods',
            name='fat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_foods',
            name='portion',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='user_foods',
            name='protein',
            field=models.FloatField(),
        ),
    ]
