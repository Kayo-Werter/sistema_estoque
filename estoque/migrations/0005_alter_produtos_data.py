# Generated by Django 5.0 on 2023-12-21 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0004_produtos_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produtos',
            name='data',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]