# Generated by Django 4.0.3 on 2022-05-03 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0008_machines_status'),
        ('customer', '0022_alter_orderdetail_order_type_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='Machine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='machine_id', to='employee.machines'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='Order_type',
            field=models.CharField(choices=[('Dry', 'Dry'), ('Wash', 'Wash')], default='Wash', max_length=4),
        ),
    ]
