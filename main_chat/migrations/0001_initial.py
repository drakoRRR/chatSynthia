# Generated by Django 4.2.7 on 2023-11-08 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatGptBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageInput', models.TextField()),
                ('bot_response', models.TextField()),
            ],
        ),
    ]
