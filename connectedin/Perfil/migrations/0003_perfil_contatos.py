# Generated by Django 3.1 on 2020-10-08 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Perfil', '0002_convite'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='contatos',
            field=models.ManyToManyField(related_name='_perfil_contatos_+', to='Perfil.Perfil'),
        ),
    ]