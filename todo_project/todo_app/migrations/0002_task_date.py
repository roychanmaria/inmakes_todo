# Generated by Django 4.1.2 on 2023-05-31 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='exit'),
            preserve_default=False,
        ),
    ]
