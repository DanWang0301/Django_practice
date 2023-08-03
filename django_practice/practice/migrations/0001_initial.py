# Generated by Django 3.2.6 on 2023-08-03 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authorized',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Authorized', models.TextField(choices=[('0', 'admin'), ('1', 'conmpany'), ('2', 'customer')])),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.TextField(max_length=100)),
                ('User_Email', models.TextField(default='guest')),
                ('User_Password', models.TextField()),
                ('User_permission', models.TextField()),
                ('last_come_date', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('User_Authorized', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to='practice.authorized')),
            ],
        ),
    ]
