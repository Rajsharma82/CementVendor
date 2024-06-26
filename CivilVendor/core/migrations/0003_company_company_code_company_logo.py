# Generated by Django 4.0 on 2024-04-21 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_company_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='company_code',
            field=models.CharField(default=str, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(default=str, upload_to='core/logo/'),
            preserve_default=False,
        ),
    ]
