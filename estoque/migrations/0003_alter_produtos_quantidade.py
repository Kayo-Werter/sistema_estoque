# Generated by Django 5.0 on 2023-12-21 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_produtos_quantidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='quantidade',
            field=models.IntegerField(default=0),
        ),
    ]
