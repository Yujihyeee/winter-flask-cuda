# Generated by Django 3.2.5 on 2021-12-13 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jeju_schedule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateField()),
                ('price', models.IntegerField()),
                ('tax', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('fees', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('jeju_schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jeju_schedule.jejuschedule')),
            ],
            options={
                'db_table': 'reservation',
            },
        ),
    ]
