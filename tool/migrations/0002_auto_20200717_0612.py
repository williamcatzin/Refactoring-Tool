# Generated by Django 3.0.8 on 2020-07-17 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commit',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='commit',
            name='body',
            field=models.CharField(max_length=500),
        ),
    ]