# Generated by Django 4.2.2 on 2023-06-16 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enexx', '0002_tipo_juego_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='juego',
            name='imagen',
            field=models.ImageField(null=True, upload_to='juegos'),
        ),
    ]
