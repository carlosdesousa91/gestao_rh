# Generated by Django 3.1.6 on 2021-09-12 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_antigo', '0002_registrousuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrousuario',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]