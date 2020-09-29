# Generated by Django 3.1.1 on 2020-09-29 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='poll',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choises', to='poll_list.poll'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
