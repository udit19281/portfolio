# Generated by Django 3.2.1 on 2021-05-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(choices=[('cabin', 'cabin'), ('cake', 'cake'), ('circus', 'circus'), ('game', 'game'), ('safe', 'safe'), ('submarine', 'submarine')], max_length=10),
        ),
    ]