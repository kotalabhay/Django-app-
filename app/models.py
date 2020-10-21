from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from app.other_constants import *
from app.utils import generate_random_string as id_generator

class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		#user.is_admin = True
		#user.is_staff = True
		#user.is_superuser = True
		#if not user.user_id:
		#	user.user_id=id_generator()
		#user.save(using=self._db)
		#while Account.objects.filter(user_id=user.user_id).exists():
		#		user.user_id = id_generator()
		#user.save(using=self._db)
		#return user
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class Account(AbstractBaseUser):
	state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
	company_choices=(("Trust","Trust"),("Proprietorship","Proprietorship"),("Pvt.Ltd","Pvt.Ltd"),("Ltd","Ltd"))
	email= models.EmailField(verbose_name="email", max_length=60, unique=True)
	country = models.CharField(max_length = 5,null = True,blank = True,db_index = True,choices = country_list.COUNTRIES_LIST_CHOICES)
	username= models.CharField(max_length=30, unique=True)
	pin_code= models.CharField(max_length=30,verbose_name = "Pincode")
	address2=models.CharField(max_length=60,verbose_name = "Address 2")
	city_name=models.CharField(max_length=17,verbose_name = "City")
	company_name=models.CharField(max_length=15,verbose_name="Company Name")
	state = models.CharField(choices=state_choices,max_length=255, null=True, blank=True)
	company_type= models.CharField(choices=company_choices,max_length=20,null=True,blank=True)
	#user_id = models.CharField(max_length=13,editable=True, unique=False, null=False)
	address1=models.CharField(max_length=50,verbose_name = "Address1")
	gst_no=models.CharField(max_length=15,verbose_name = "Gst no")

	pan_no=models.CharField(max_length=15,verbose_name="PAN_NO")
	tan_no=models.CharField(max_length=15,verbose_name="TAN_NO")
	mobile_no=models.CharField(max_length=10,verbose_name="mobile_no")
	telephone_no=models.CharField(max_length=10,verbose_name="telephone_no")
	company_registry_no=models.CharField(max_length=15,verbose_name="Company Registry No")
	Currency_denomination = models.CharField(max_length=3, default='Rs', editable=True)
	date_joined	= models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login=models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin= models.BooleanField(default=False)
	is_active= models.BooleanField(default=True)
	is_staff= models.BooleanField(default=False)
	is_superuser= models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_perms(self, app_label):
		return True

	#def saving(self):
		#if not self.user_id:
			# Generate ID once, then check the database. If exists, keep trying.
			#self.user_id = id_generator()
			#while Account.objects.filter(user_id=self.user_id).exists():
			#	self.user_id = id_generator()
		#super(Account, self).save()