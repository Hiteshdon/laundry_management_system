# Generated by Django 4.0.3 on 2022-04-06 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0005_dressesdetail_alter_userdetail_id_orderdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryDetail',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('Supply_Name', models.CharField(max_length=20, unique=True)),
                ('Quantity', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'InventoryDetail',
                'verbose_name_plural': 'InventoryDetails',
            },
        ),
        migrations.CreateModel(
            name='OrderDresses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.PositiveSmallIntegerField(default=0)),
                ('cost', models.PositiveIntegerField()),
                ('Dress_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dress_id', to='customer.dressesdetail')),
                ('Order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_id', to='customer.orderdetail')),
            ],
            options={
                'verbose_name': 'OrderDresses',
                'verbose_name_plural': 'OrderDresses',
            },
        ),
    ]
