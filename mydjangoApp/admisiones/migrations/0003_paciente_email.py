# Generated by Django 4.0.3 on 2022-03-30 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admisiones', '0002_paciente_create_paciente_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True),
        ),
    ]
