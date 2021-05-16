# Generated by Django 3.2.3 on 2021-05-16 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('atracoes', '0001_initial'),
        ('comentarios', '0001_initial'),
        ('avaliacoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('is_approved', models.BooleanField(default=False)),
                ('atracoes', models.ManyToManyField(to='atracoes.Atracao')),
                ('avaliacoes', models.ManyToManyField(to='avaliacoes.Avaliacao')),
                ('comentarios', models.ManyToManyField(to='comentarios.Comentario')),
            ],
            options={
                'verbose_name': 'Ponto Turístico',
                'verbose_name_plural': 'Pontos Turísticos',
            },
        ),
    ]