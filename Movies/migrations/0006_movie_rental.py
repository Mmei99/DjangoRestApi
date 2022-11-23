# Generated by Django 4.1.3 on 2022-11-19 00:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0005_alter_rental_rental_id_delete_movie_rental'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rental_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movies.rental')),
            ],
        ),
    ]
