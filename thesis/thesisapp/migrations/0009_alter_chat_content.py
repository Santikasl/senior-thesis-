# Generated by Django 4.1.5 on 2023-06-07 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesisapp', '0008_chat_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
