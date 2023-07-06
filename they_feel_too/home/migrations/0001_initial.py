# Generated by Django 4.2.2 on 2023-07-05 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('promedio_de_vida', models.CharField(help_text='Puede escribir tanto en cautiverio como salvaje', max_length=100)),
                ('alimentacion', models.CharField(help_text='En que se basa la alimentación del animal', max_length=100)),
                ('imagen', models.CharField(help_text='Link a la imagen del animal', max_length=100)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Consejo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Consejos para preservar la flora y fauna del planeta', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Habitat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('continente', models.CharField(choices=[('AF', 'Africa'), ('AS', 'Asia'), ('AM', 'America'), ('EU', 'Europa'), ('OC', 'Oceania'), ('AN', 'Antartida')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt', models.CharField(help_text='Texto auxiliar por si la imagen se encuentra caida', max_length=200)),
                ('estilo', models.CharField(max_length=100)),
                ('imagen', models.TextField(help_text='Link a la imagen')),
            ],
        ),
        migrations.CreateModel(
            name='Curiosidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(help_text='Curiosidad del animal', max_length=200)),
                ('animal', models.ForeignKey(help_text='Animal al que pertenece esta curiosidad', on_delete=django.db.models.deletion.CASCADE, to='home.animal')),
            ],
        ),
        migrations.AddField(
            model_name='animal',
            name='habitats',
            field=models.ManyToManyField(help_text='Habitats a los que pertenece el animal', to='home.habitat'),
        ),
    ]
