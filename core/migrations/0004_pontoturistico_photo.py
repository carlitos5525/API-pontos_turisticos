# Generated by Django 3.2.3 on 2021-05-22 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_pontoturistico_enderecos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pontos_turisticos'),
        ),
    ]
