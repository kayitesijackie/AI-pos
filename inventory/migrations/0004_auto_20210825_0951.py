# Generated by Django 2.2 on 2021-08-25 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20201224_1558'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='order',
            name='cart_tax',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='tax',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tax_rate',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='tax_type',
            field=models.CharField(blank=True, choices=[('B-EX', 'B-EX'), ('A-EX', 'A-EX')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='payment_mode',
            field=models.CharField(blank=True, choices=[('cash', 'Cash'), ('mobicash', 'MobiCash'), ('mm', 'Mobile Money'), ('carte', 'Carte de debit'), ('tb', 'Transfer bancaire'), ('cheque', 'Cheque')], default='Cash', max_length=10, null=True),
        ),
    ]
