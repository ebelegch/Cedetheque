# Generated by Django 2.0.4 on 2018-05-27 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='musique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_album', models.CharField(max_length=300)),
                ('num_piste', models.CharField(max_length=1)),
                ('titre', models.CharField(max_length=300)),
                ('auteur', models.CharField(max_length=300)),
                ('compositeur', models.CharField(max_length=300)),
                ('interprete', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
