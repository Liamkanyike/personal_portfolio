# Generated by Django 2.2.4 on 2019-09-03 06:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfolio_portfolio_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
    ]
