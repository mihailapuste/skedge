# Generated by Django 3.1 on 2020-08-08 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=50)),
                ('short_description', models.CharField(max_length=200, null=True)),
                ('long_description', models.CharField(max_length=3000, null=True)),
                ('contact_email', models.CharField(max_length=50, null=True)),
                ('phone_number', models.CharField(max_length=14, null=True)),
                ('category', models.CharField(choices=[('all', 'All'), ('fitness', 'Fitness'), ('wellness', 'Wellness'), ('beauty', 'Beauty'), ('miscellaneous', 'Miscellaneous')], default='miscellaneous', max_length=50)),
                ('address', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('postal_code', models.CharField(max_length=6, null=True)),
                ('country', models.CharField(max_length=100, null=True)),
                ('monday_open', models.BooleanField(default=True)),
                ('tuesday_open', models.BooleanField(default=True)),
                ('wednesday_open', models.BooleanField(default=True)),
                ('thursday_open', models.BooleanField(default=True)),
                ('friday_open', models.BooleanField(default=True)),
                ('saturday_open', models.BooleanField(default=False)),
                ('sunday_open', models.BooleanField(default=False)),
                ('monday_opening_time', models.TimeField(default='9:00')),
                ('tuesday_opening_time', models.TimeField(default='9:00')),
                ('wednesday_opening_time', models.TimeField(default='9:00')),
                ('thursday_opening_time', models.TimeField(default='9:00')),
                ('friday_opening_time', models.TimeField(default='9:00')),
                ('saturday_opening_time', models.TimeField(default='9:00')),
                ('sunday_opening_time', models.TimeField(default='9:00')),
                ('monday_closing_time', models.TimeField(default='17:00')),
                ('tuesday_closing_time', models.TimeField(default='17:00')),
                ('wednesday_closing_time', models.TimeField(default='17:00')),
                ('thursday_closing_time', models.TimeField(default='17:00')),
                ('friday_closing_time', models.TimeField(default='17:00')),
                ('saturday_closing_time', models.TimeField(default='17:00')),
                ('sunday_closing_time', models.TimeField(default='17:00')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='', max_length=14)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('duration', models.IntegerField(choices=[(15, '15'), (30, '30'), (45, '45'), (60, '1:00'), (90, '1:30'), (120, '2:00'), (150, '2:30'), (180, '3:00')])),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.business')),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.business')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('cancelled', models.BooleanField(default=False)),
                ('cancelled_by_customer', models.BooleanField(default=False)),
                ('cancelled_by_business', models.BooleanField(default=False)),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.business')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.customer')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.service')),
            ],
        ),
    ]
