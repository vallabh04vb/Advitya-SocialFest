# Generated by Django 4.2.1 on 2024-01-13 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Advitya_app', '0015_alter_useractivityregistration_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=12)),
                ('college', models.CharField(default='', max_length=200)),
                ('City', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('profession', models.CharField(default='', max_length=50)),
                ('referral', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
