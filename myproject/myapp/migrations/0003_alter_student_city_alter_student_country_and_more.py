# Generated by Django 4.2.7 on 2023-11-21 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_city_city_id_remove_country_country_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.city'),
        ),
        migrations.AlterField(
            model_name='student',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.country'),
        ),
        migrations.AlterField(
            model_name='student',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.state'),
        ),
    ]
