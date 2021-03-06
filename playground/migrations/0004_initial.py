# Generated by Django 4.0.1 on 2022-01-21 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('playground', '0003_delete_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('discord_handle', models.CharField(blank=True, max_length=200)),
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(blank=True, max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.CharField(blank=True, choices=[('DSA', 'DSA'), ('Level1', 'Level1'), ('Level2', 'Level2')], max_length=200)),
            ],
        ),
    ]
