# Generated by Django 4.2.3 on 2023-07-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
                ('imagen', models.ImageField(upload_to='')),
                ('link', models.URLField()),
                ('web', models.BooleanField()),
                ('ciencia_de_datos', models.BooleanField()),
                ('analisis_de_datos', models.BooleanField()),
                ('tranding', models.BooleanField()),
            ],
        ),
    ]
