# Generated by Django 5.0.7 on 2024-11-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('silver', models.IntegerField()),
                ('gold', models.IntegerField()),
            ],
        ),
    ]
