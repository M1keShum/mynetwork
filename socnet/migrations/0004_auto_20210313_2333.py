# Generated by Django 3.1.2 on 2021-03-13 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socnet', '0003_auto_20210313_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Сообщение'),
        ),
    ]
