# Generated by Django 2.2 on 2020-05-12 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Centermaster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='center_master',
            name='Project_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='center_master', to='project_master.Project_Master'),
        ),
    ]