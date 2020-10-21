from django.forms import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from app.models import Account
#from django.contrib.auth import get_user_model
from app.models import *
from app.other_constants import *
from django.contrib.auth import authenticate


class RegisterForm(UserCreationForm):
	
	

	class Meta:
		model = Account
		#fields = ["username", "email", "password1", "password2","pin_code","area_name","state","company_type","pan_no","tan_no","mobile_no","telephone_no","company_registry_no",]
		fields = ["username", "email", "password1", "password2","pin_code","pan_no","city_name","company_name","tan_no","mobile_no","telephone_no","company_registry_no","state","country","company_type",'address1','Currency_denomination','address2','gst_no']
		state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
		company_choices=(("Trust","Trust"),("Proprietorship","Proprietorship"),("Pvt.Ltd","Pvt.Ltd"),("Ltd","Ltd"))
		exclude = ('Currency_denomination',)

		widgets = {

			'state' : Select(attrs={'class':'form-control input-sm'}, choices=state_choices),
			'country' : Select(attrs={'class':'form-control input-sm'}, choices = country_list.COUNTRIES_LIST_CHOICES),
			'company_type' : Select(attrs={'class':'form-control input-sm'}, choices=company_choices),
			'username':TextInput(attrs={'class':'input--style-2', 'max_length':'20','name':'username'}),
			'email':TextInput(attrs={'class':'input--style-2', 'max_length':'20','name':'email'}),
			'password1':TextInput(attrs={'class':'input--style-2', 'max_length':'20','name':'password1'}),
			'password2':TextInput(attrs={'class':'input--style-2', 'max_length':'20','name':'password2'}),
			#'user_id':TextInput(attrs={'class':'form-control', 'max_length':'20','placeholder':'user_id','name':'user_id'}),
			'company_name':TextInput(attrs={'class':'input--style-2', 'max_length':'20','name':'company_name'}),
			'pan_no':TextInput(attrs={'class':'input--style-2','onblur':'ValidatePAN(this)','id':'pan', 'max_length':'15','name':'organisation_pan','type':'text'}),
			'tan_no':TextInput(attrs={'class':'input--style-2', 'max_length':'15','name':'tan_no'}),
			'mobile_no':TextInput(attrs={'class':'input--style-2','type':'tel','required':'required','max_length':'20','name':'mobile_no'}),
			'telephone_no':TextInput(attrs={'class':'input--style-2','type':'tel','required':'required', 'max_length':'20','name':'telephone_no'}),
			'address1':TextInput(attrs={'class':'input--style-2', 'max_length':'50','name':'address2'}),
			'address2':TextInput(attrs={'class':'input--style-2', 'max_length':'50','name':'address2'}),
			'gst_no':TextInput(attrs={'class':'input--style-2', 'max_length':'15','name':'gst_no'}),


			'city_name':TextInput(attrs={'class':'input--style-2', 'max_length':'15','name':'city_name'}),
			'company_registry_no':TextInput(attrs={'class':'input--style-2', 'max_length':'15','name':'company_registry_no'}),
			'pin_code':TextInput(attrs={'class':'input--style-2', 'max_length':'8','name':'pin_code'}),
		

			}

	def save(self,commit=True):
		user=super(RegisterForm,self).save(commit=False)
		user.email=self.cleaned_data['email']
		user.country=self.cleaned_data['country']
		user.pin_code=self.cleaned_data['pin_code']
		user.company_type=self.cleaned_data['company_type']
		#user.user_id=self.cleaned_data['user_id']
		user.country=self.cleaned_data['country']
		user.username=self.cleaned_data['username']
		user.pan_no=self.cleaned_data['pan_no']
		user.address1=self.cleaned_data['address1']
		user.address2=self.cleaned_data['address2']
		user.gst_no=self.cleaned_data['gst_no']
		user.city_name=self.cleaned_data['city_name']
		user.company_name=self.cleaned_data['company_name']
		user.tan_no=self.cleaned_data['tan_no']
		user.mobile_no=self.cleaned_data['mobile_no']
		user.telephone_no=self.cleaned_data['telephone_no']
		user.company_registry_no=self.cleaned_data['company_registry_no']
		#user.Currency_denomination=self.cleaned_data['Currency_denomination']
		user.password1=self.cleaned_data['password1']
		user.password2=self.cleaned_data['password2']

		if commit:
			user.save()
		return user


class AccountAuthenticationForm(forms.ModelForm):

	password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'input100', 'max_length':'20','placeholder':'Password','name':'pass','type':'password'}))

	class Meta:
		model = Account
		fields = ('email', 'password',)
		widgets={
			'email':TextInput(attrs={'class':'input100', 'max_length':'20','placeholder':'Email','name':'email'}),
			'password':PasswordInput(attrs={'class':'input100', 'max_length':'20','placeholder':'Password','name':'pass','type':'password'}),
		}

	def clean(self):
		if self.is_valid():
			email = self.cleaned_data['email']
			password = self.cleaned_data['password']
			if not authenticate(email=email, password=password):
				raise forms.ValidationError("Invalid login")