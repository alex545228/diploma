# Generated by Django 3.1.3 on 2020-11-29 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pallada_app', '0004_auto_20201128_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='scrappeddata',
            name='social_id',
            field=models.CharField(default=0, max_length=255, verbose_name='Social id for user'),
            preserve_default=False,
        ),
    ]