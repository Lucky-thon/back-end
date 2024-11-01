# Generated by Django 5.1.2 on 2024-10-29 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_missions', '0003_dailymission_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailymission',
            name='last_updated',
        ),
        migrations.AddField(
            model_name='dailymission',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='dailymission',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='dailymission',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='dailymission',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='dailymission',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
