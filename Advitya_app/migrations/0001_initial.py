# Generated by Django 4.2.1 on 2023-12-30 05:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('activity_type', models.CharField(choices=[('Activity 1', 'Activity 1'), ('Activity 2', 'Activity 2')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Socio_trivia_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(default='', max_length=200)),
                ('address', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserActivityRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(default='no', max_length=50)),
                ('phone_number', models.CharField(max_length=15)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Advitya_app.activity')),
            ],
        ),
    ]
