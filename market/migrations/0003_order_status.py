# Generated by Django 4.1.4 on 2023-01-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(default='created', max_length=100),
        ),
    ]
