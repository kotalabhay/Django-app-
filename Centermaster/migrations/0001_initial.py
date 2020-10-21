# Generated by Django 2.2 on 2020-05-12 16:06

import Centermaster.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project_master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Center_Master',
            fields=[
                ('pia_name', models.CharField(max_length=150, unique=True)),
                ('project_name', models.CharField(max_length=30, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Name_District', models.CharField(max_length=150)),
                ('Assembly_Constituency', models.CharField(max_length=150)),
                ('Parliamentary_Constituency', models.CharField(max_length=150)),
                ('Name_of_training_Center', models.CharField(max_length=150)),
                ('Training_Centode_Alias', models.CharField(max_length=150)),
                ('Address1_Training_Center', models.CharField(max_length=150)),
                ('Address2_Training_Center', models.CharField(max_length=150)),
                ('Mobile_No_TC_Manager', models.CharField(max_length=150)),
                ('Email_id_TC_Manager', models.CharField(max_length=150)),
                ('Distance_From_Bus_Stand', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Distance_From_Auto_Stand', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Distance_From_Railway_Station', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Distance_From_Airport', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Latitude', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Longitude', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Photograph_Building_Sign', models.ImageField(blank=True, null=True, upload_to=Centermaster.models.upload_location)),
                ('Photograph_adjoining_building', models.ImageField(blank=True, null=True, upload_to=Centermaster.models.upload_location)),
                ('Ownership_of_the_Building', models.CharField(max_length=150)),
                ('Owner_Name_of_the_Building', models.CharField(max_length=150)),
                ('Area_of_the_Building', models.IntegerField(blank=True, db_index=True, null=True)),
                ('RCC', models.CharField(blank=True, choices=[('RCC', 'RCC'), ('Not RCC', 'Not RCC')], max_length=55, null=True)),
                ('Circulation_Area', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Open_space_Area', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Exlcusive_Bicycle_Parking', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Open_Space_Security', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Rooms_Available_Number', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Number_Of_Toilets', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Number_Of_Corridor', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='center_master', to='project_master.Project_Master')),
            ],
            options={
                'verbose_name_plural': 'center_master_details_tbl',
            },
        ),
        migrations.CreateModel(
            name='ToiletTable',
            fields=[
                ('Toilet_Sr_Number', models.AutoField(primary_key=True, serialize=False)),
                ('Light_No', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Lights_Image', models.ImageField(blank=True, null=True, upload_to=Centermaster.models.upload_location)),
                ('Type_Flooring', models.CharField(max_length=150)),
                ('Flooring_Image', models.ImageField(blank=True, null=True, upload_to=Centermaster.models.upload_location)),
                ('Connection_running_water', models.CharField(max_length=150)),
                ('Toilet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Centermaster.Center_Master')),
            ],
        ),
        migrations.CreateModel(
            name='Roomtable',
            fields=[
                ('Room_Sr_Number', models.AutoField(primary_key=True, serialize=False)),
                ('Room_Length', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Room_Width', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Room_Area', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Roof_Height', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Windows_Areas', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Centermaster.Center_Master')),
            ],
        ),
        migrations.CreateModel(
            name='CorridorTable',
            fields=[
                ('Corridor_Sr_Number', models.AutoField(primary_key=True, serialize=False)),
                ('Length_Of_Corridor', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Width_Of_Corridor', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Area_Of_Corridor', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Roof_Height_Corridor', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Windows_Areas', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Number_of_Lights', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Number_Of_Fans', models.IntegerField(blank=True, db_index=True, null=True)),
                ('Corridor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Centermaster.Center_Master')),
            ],
        ),
    ]
