# Generated by Django 4.0.1 on 2022-01-22 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0006_customer_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resources',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='category',
            field=models.CharField(blank=True, choices=[('DSA1', 'DSA1'), ('DSA2', 'DSA2'), ('CP1', 'CP1'), ('CP2', 'CP2')], max_length=200),
        ),
    ]
