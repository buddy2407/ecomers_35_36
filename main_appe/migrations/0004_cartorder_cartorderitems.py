# Generated by Django 4.1.2 on 2022-10-29 09:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_appe', '0003_remove_product_image_productattributes_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='cartorder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.FloatField()),
                ('paid_status', models.BooleanField(default=False)),
                ('order_dt', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '8. orders',
            },
        ),
        migrations.CreateModel(
            name='cartorderitems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_num', models.CharField(max_length=350)),
                ('item', models.CharField(max_length=300)),
                ('image', models.CharField(max_length=300)),
                ('qty', models.IntegerField()),
                ('price', models.FloatField()),
                ('total', models.FloatField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_appe.cartorder')),
            ],
            options={
                'verbose_name_plural': '9. order items',
            },
        ),
    ]
