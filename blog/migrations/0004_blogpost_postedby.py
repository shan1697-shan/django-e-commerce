# Generated by Django 3.0.4 on 2020-04-05 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blogpost_items_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='postedby',
            field=models.CharField(default='', max_length=80),
        ),
    ]
