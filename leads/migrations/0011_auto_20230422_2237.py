# Generated by Django 3.1.4 on 2023-04-22 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0010_auto_20230422_2211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
