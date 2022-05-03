# Generated by Django 4.0.3 on 2022-04-06 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_dressesdetail_alter_userdetail_id_orderdetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetail',
            name='role',
            field=models.CharField(choices=[('customer', 'Customer'), ('employee', 'Employee'), ('Manager', 'Manager')], default='Customer', max_length=8),
        ),
    ]
