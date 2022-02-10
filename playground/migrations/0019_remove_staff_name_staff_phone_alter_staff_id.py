# Generated by Django 4.0.1 on 2022-01-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0018_staff_date_created_staff_discord_handle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='name',
        ),
        migrations.AddField(
            model_name='staff',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=models.PositiveIntegerField(primary_key=True, serialize=False),
        ),
    ]
