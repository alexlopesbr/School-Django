# Generated by Django 4.2.5 on 2023-10-01 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_number', models.CharField(choices=[('1', 'Year 1'), ('2', 'Year 2'), ('3', 'Year 3'), ('4', 'Year 4'), ('5', 'Year 5'), ('6', 'Year 6'), ('7', 'Year 7'), ('8', 'Year 8'), ('9', 'Year 9'), ('10', 'Year 10'), ('11', 'Year 11'), ('12', 'Year 12'), ('1', 'Year 1'), ('2', 'Year 2'), ('3', 'Year 3'), ('4', 'Year 4'), ('5', 'Year 5'), ('6', 'Year 6'), ('7', 'Year 7'), ('8', 'Year 8'), ('9', 'Year 9'), ('10', 'Year 10'), ('11', 'Year 11'), ('12', 'Year 12')], max_length=15)),
                ('year_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='SchoolClassUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.schoolclass')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
