from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from app.utils import generate_random_string as id_generator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


def upload_location(instance, filename):
	file_path = 'media/{user_id}/{title}-{filename}'.format(
				user_id=str(instance.user.id),title=str(instance.project_name), filename=filename)
	return file_path

#def project_id_maker():
	#project_id = Project_Master.objects.all().values('project_id')
	#if not project_id:
			# Generate ID once, then check the database. If exists, keep trying.
		#project_id = id_generator()
		#while Project_Master.objects.filter(project_id=project_id).exists():
			#project_id = id_generator()
	#return project_id

	
class Project_Master(models.Model):
	Single_Consortium_CHOICES = (('Single', 'Single'),('Consortium', 'Consortium'))
	PER_Choices=((True, 'Yes'),(False, 'No'))
	PPWS_Choices=((True, 'Yes'),(False, 'No'))
	tlm_Choices=(("Approved","Approved"),("Not Approved","Not Approved"))

	state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL, 
		db_index = True, 
		on_delete = models.CASCADE,
		null = True,
		blank = True,
		related_name="project_master"
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

	sanction_order_number=models.CharField(
		max_length=150,      #done
		null=False,
		blank=False,
		unique=True,
		
	)
	sanction_order_date=models.DateField(
		db_index=True,
	)

	proposal_code=models.CharField(
		max_length=40,
		null=False,
		blank=False,
		unique=True,
	)

	project_duration=models.CharField(
		max_length=2,
		null=False,
		blank=False,
		#unique=True,

	)
	state = models.CharField(
		choices=state_choices,
		max_length=255,
		null=True, 
		blank=True
	)

	Company_owner_type= models.CharField(
		choices=Single_Consortium_CHOICES,
		max_length=255,
		null=True, 
		blank=True
	)
	partner_name= models.CharField(
		max_length=50,
		blank=True,
		null=False,
	)
	training_target=models.IntegerField(
		db_index=True,
		#blank=False,
		null=False,


	)

	project_cost = models.DecimalField(
		max_digits=30,
		 decimal_places=2,
	)

	date_pac_approval=models.DateField(
		db_index=True,
	)

	date_pco=models.DateField(
		db_index=True,
	)

	date_mou=models.DateField(
		db_index=True,
	)

	date_commencement=models.DateField(
		db_index=True,
	)
	date_last_training_completition=models.DateField(
		db_index=True,
	)

	date_last_placement_completion=models.DateField(
		db_index=True,
	)

	date_project_end=models.DateField(
		db_index=True,
	)

	is_PER_approved = models.BooleanField(
		db_index = True,
		choices =PER_Choices,
		default = False,
	)

	PER_date=models.DateField(
		db_index=True,
	)

	is_PPWS_approved= models.BooleanField(
		db_index = True,
		choices =PPWS_Choices,
		default = False,
	)


	PPWS_date=models.DateField(
		db_index=True,
	)

	alloted_trade=models.CharField(
		max_length=30,
		null=False,
		blank=False,
		unique=True,
		
	)


	alloted_trade_target=models.IntegerField(
		db_index=True,
		#blank=False,
		null=False,
	)



	mobilization_district=models.CharField(
		max_length=150,
		null=False,
		blank=False,
		#unique=True,
	)

	mobilization_target=models.IntegerField(
		null=False,
		blank=False,
		db_index=True,	
	)

	project_id = models.CharField(
		max_length=20,
		editable=False,
		unique=True,
		null=False,
		primary_key=True,
		#default=project_id_maker,
		)
	

	tlm_approved_status=  models.CharField(
		choices=tlm_Choices,
		max_length=100,
		null=True, 
		blank=True,
	)
	

	image= models.ImageField(
		upload_to=upload_location,
		null=True,
		blank=True
	)


	def is_PER_approved_full(self):
		if self.is_PER_approved:
			return "YES"
		return "NO"

	def is_PPWS_approved_full(self):
		if self.is_PPWS_approved:
			return "YES"
		return "NO"

	def get_tc_district(self):
		return ', '.join(self.Project_Master.all().values_list('tc_district', flat=True))

	def get_tc_target(self):
		return ', '.join(self.Project_Master.all().values_list('trade_target', flat=True))



	def save(self):
		if not self.project_id:
			# Generate ID once, then check the database. If exists, keep trying.
			self.project_id = id_generator()
			while Project_Master.objects.filter(project_id=self.project_id).exists():
				self.project_id = id_generator()
		super(Project_Master, self).save()

	def __str__(self):
		return self.project_id



	class Meta:
		verbose_name_plural = 'project_master_details_tbl'

@receiver(post_delete, sender=Project_Master)
def submission_delete(sender, instance, **kwargs):
	instance.image.delete(False) 






class Tc_Details(models.Model):
	trade_target=models.IntegerField(
		null=True,
		blank=True,
		db_index=True,
	)

	tc_district=models.CharField(
		max_length=150,
		null=True,
		blank=True,
		#unique=True,
	)

	tc = models.ForeignKey(
		Project_Master,
		related_name='Project_Master', on_delete=models.CASCADE,
		null=True
	)
	
	def __str__(self):
		#return str(self.id)
		return f'{self.id}'

	#def save_model(self, request, obj, form, change):
    	#obj.added_by = request.project_id
    	#super().save_model(request, obj, form, change)

	class Meta:
		db_table = 'tc_details'

