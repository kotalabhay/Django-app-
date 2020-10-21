from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from app.utils import generate_random_string as id_generator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from project_master.models import *
from datetime import datetime

now = datetime.now()

# def upload_location(instance, filename):
# 	file_path = 'media/project/{Project_id}/{title}-{filename}'.format(
# 				project_id=str(instance.Project_id),title=str(instance.project_name), filename=filename)
# 	return file_path

def upload_location(instance, filename):
	return f'media/{now.year}/{now.month}/{now.date().day}/{filename}'

class Center_Master(models.Model):
	
	RCC_CHOICES = (('RCC', 'RCC'),('Not RCC', 'Not RCC'))
	state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
	Project_id = models.ForeignKey(
		Project_Master, 
		db_index = True, 
		blank=True,
		null=True,
		on_delete = models.CASCADE,
		related_name="center_master"
	)

	pia_name=models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
		unique=True,
	)

	project_name=models.CharField(
		max_length=30,
		null=False,			#done
		blank=False,
		unique=True,
	)

	id=models.AutoField(
		primary_key=True
		)
	# project_id = models.CharField(
	# 	max_length=20,
	# 	editable=False,
	# 	unique=True,
	# 	null=False,
	# 	primary_key=True,
	# 	#default=project_id_maker,
	# 	)

	Name_District=models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
	)

	Assembly_Constituency=models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
	)
	Parliamentary_Constituency=models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
	)

	Name_of_training_Center=models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
	)

	Training_Centode_Alias=models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
	)

	Address1_Training_Center=models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
	)

	Address2_Training_Center=models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
	)

	Mobile_No_TC_Manager=models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
	)    
	
	Email_id_TC_Manager=models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
	)

	Distance_From_Bus_Stand=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)

	Distance_From_Auto_Stand=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)
	Distance_From_Railway_Station=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)

	Distance_From_Airport=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)

	Latitude=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)

	Longitude=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)


	Photograph_Building_Sign= models.ImageField(
		upload_to=upload_location,
		null=True,
		blank=True
	)


	Photograph_adjoining_building= models.ImageField(
		upload_to=upload_location,
		null=True,
		blank=True
	)


	Ownership_of_the_Building=models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
	)
	Owner_Name_of_the_Building=models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
	)
	Area_of_the_Building=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)

	RCC = models.CharField(
		choices=RCC_CHOICES,
		max_length=55,
		null=True, 
		blank=True
	)

	Circulation_Area=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)

	Open_space_Area=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)
	Exlcusive_Bicycle_Parking=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)
	Open_Space_Security=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)
	Rooms_Available_Number=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)
	Number_Of_Toilets=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)
	Number_Of_Corridor=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)


	# def save(self):
	# 	if not self.project_id:
	# 		# Generate ID once, then check the database. If exists, keep trying.
	# 		self.project_id = id_generator()
	# 		while Company_Master.objects.filter(project_id=self.project_id).exists():
	# 			self.project_id = id_generator()
	# 	super(Company_Master, self).save()

	def __str__(self):
		return  f'{self.id}'



	class Meta:
		verbose_name_plural = 'center_master_details_tbl'

@receiver(post_delete, sender=Center_Master)
def submission_delete(sender, instance, **kwargs):
	instance.Photograph_Building_Sign.delete(False)
	instance.Photograph_adjoining_building.delete(False)  





class Roomtable(models.Model):

	 Room = models.ForeignKey(
	 Center_Master,
	 on_delete=models.CASCADE,
	 blank=True,
	 null=True,

	)

	 Room_Sr_Number=models.AutoField(
		primary_key=True,
	)
	
	 Room_Length=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)
	 Room_Width=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)

	 Room_Area=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)

	 Roof_Height=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)

	 Windows_Areas=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)



	
class ToiletTable(models.Model):

	Toilet = models.ForeignKey(
	 Center_Master, on_delete=models.CASCADE,
	 blank=True,
	 null=True,
	 )

	Toilet_Sr_Number=models.AutoField(
		primary_key=True
	)
	Light_No=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)
	Lights_Image= models.ImageField(
		upload_to=upload_location,
		null=True,
		blank=True
	)


	Type_Flooring =models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
	)

	Flooring_Image= models.ImageField(
		upload_to=upload_location,
		null=True,
		blank=True
	)

	Connection_running_water=models.CharField(
		max_length=150,
		null=False,
		blank=False,			#done
	)
	
class CorridorTable(models.Model):

	Corridor = models.ForeignKey(
	 Center_Master,
	 on_delete=models.CASCADE,
	 blank=True,
	 null=True,
	 )


	Corridor_Sr_Number=models.AutoField(
		primary_key=True,
	)

	Length_Of_Corridor=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)
	Width_Of_Corridor=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)

	Area_Of_Corridor=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)
	
	Roof_Height_Corridor=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)
	Windows_Areas=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)
	Number_of_Lights=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)

	Number_Of_Fans=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)


