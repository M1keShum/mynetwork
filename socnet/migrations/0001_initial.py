# Generated by Django 3.1.2 on 2021-03-12 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=20, null=True, verbose_name='Имя')),
                ('sname', models.TextField(blank=True, max_length=30, null=True, verbose_name='Фамилия')),
                ('birthday', models.DateField(db_index=True, verbose_name='День рождения')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'ordering': ['name'],
            },
        ),
    ]
