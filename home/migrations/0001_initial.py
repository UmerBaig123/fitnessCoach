# Generated by Django 4.2.13 on 2024-05-21 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_name', models.CharField(max_length=100)),
                ('food_description', models.TextField()),
                ('food_calories', models.IntegerField()),
                ('food_fat', models.IntegerField()),
                ('food_protein', models.IntegerField()),
                ('food_carbs', models.IntegerField()),
            ],
        ),
    ]
