# Generated by Django 2.2.12 on 2022-11-22 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Barang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kodebrg', models.CharField(max_length=8)),
                ('nama', models.CharField(max_length=50)),
                ('stok', models.IntegerField()),
                ('harga', models.BigIntegerField()),
                ('link_gbr', models.CharField(blank=True, default='img/', max_length=150)),
                ('waktu_posting', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
