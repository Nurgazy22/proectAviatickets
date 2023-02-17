# Generated by Django 4.1.7 on 2023-02-17 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=200, unique=True, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, max_length=30, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('country', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='Packets.category')),
            ],
        ),
        migrations.CreateModel(
            name='Packet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paket_title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='media/packet_image/')),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('availability', models.IntegerField()),
                ('in_stock', models.BooleanField()),
                ('quantity', models.IntegerField()),
                ('schedule', models.FileField(upload_to='')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pakets', to='Packets.hotel')),
                ('paket_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pakets', to='Packets.category')),
            ],
        ),
        migrations.CreateModel(
            name='PacketImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='media/packet_image/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('packet_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Packets.packet')),
            ],
        ),
    ]
