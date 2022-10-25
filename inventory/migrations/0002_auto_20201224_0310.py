# Generated by Django 3.1.2 on 2020-12-24 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCompany',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'ProductCompany',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.productcompany'),
        ),
    ]
