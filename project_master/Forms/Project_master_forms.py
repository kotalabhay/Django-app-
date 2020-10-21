from django.forms import *
from django import forms
from project_master.models import *
#from django.contrib.auth.models import User
#from project_master.models.project_master_model import *
#from django.contrib.auth import get_user_model
from app.other_constants import *
from django.contrib.auth import authenticate
from django.forms import modelformset_factory


Project_MasterFormset = modelformset_factory(
	Tc_Details,
	fields=('trade_target','tc_district', ),
	extra=1,
	widgets={'tc_district': forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Enter  TC District here'}),

			'trade_target': forms.NumberInput(attrs={
			'class': 'form-control',
			'placeholder': 'Enter  Trade Target here'}),
		})
	



class Project_MasterForm(forms.ModelForm):
	class Meta:
		model = Project_Master
		fields = '__all__'
		exclude=('project_id','user',)

		Single_Consortium_CHOICES = (('Single', 'Single'),('Consortium', 'Consortium'))
		PER_Choices=((True, 'Yes'),(False, 'No'))
		PPWS_Choices=((True, 'Yes'),(False, 'No'))
		tlm_Choices=(("Approved","Approved"),("Not Approved","Not Approved"))

		state_choices = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))
		widgets = {
			'pia_name' : TextInput(attrs={'class':'form-control', 'max_length':'150','required':'required'}),
			'project_name' : TextInput(attrs={'class':'form-control', 'max_length':'30','required':'required'}),
			'sanction_order_number' : TextInput(attrs={'class':'form-control', 'max_length':'150','required':'required'}),
			'sanction_order_date': forms.DateInput(format=('%d-%m-%Y'),attrs={'class':' input--style-2   ', 'placeholder':'  YYYY-MM-DD','required':'required','type':'text','required pattern':'[0-9]{4}-[0-9]{2}-[0-9]{2}' }),
			'proposal_code' : TextInput(attrs={'class':'form-control', 'max_length':'40','required':'required'}),
			'project_duration' : TextInput(attrs={'class':'form-control', 'max_length':'150','required':'required'}),
			#'pia_name' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'150','required':'required'}),
			'state' : Select(attrs={'class':'form-control input-sm',}, choices = state_choices, ),
			'Company_owner_type' :Select(attrs={'class':'select form-control','onchange':'yesnoCheck(this);',}, choices = Single_Consortium_CHOICES, ),
			#'is_Consortium' : forms.ChoiceField(widget=forms.RadioSelect, choices = Single_Consortium_CHOICES, ),
			'partner_name' : TextInput(attrs={'class':'form-control', 'max_length':'50','id':'ifYes'}),
			'training_target' : NumberInput(attrs={'class':'form-control','required':'required'}),
			'project_cost' : NumberInput(attrs={'class':'form-control','required':'required'}),
			'date_pac_approval': forms.DateInput(format=('%d-%m-%Y'),attrs={'class':' input--style-2  ', 'placeholder':'  YYYY-MM-DD','required':'required'}),
			'date_pco': forms.DateInput(format=('%d-%m-%Y'),attrs={'class':' input--style-2  ', 'placeholder':'  YYYY-MM-DD','required':'required'}),
			'date_mou': forms.DateInput(format=('%d-%m-%Y'),attrs={'class':' input--style-2  ', 'placeholder':'  YYYY-MM-DD','required':'required'}),
			'date_commencement': forms.DateInput(format=('%d-%m-%Y'),attrs={'class':' input--style-2  ', 'placeholder':'  YYYY-MM-DD','required':'required'}),
			'date_last_training_completition': forms.DateInput(format=('%d-%m-%Y'),attrs={'class':' input--style-2  ', 'placeholder':'  YYYY-MM-DD','required':'required'}),
			'date_last_placement_completion': forms.DateInput(format=('%d-%m-%Y'),attrs={'class':' input--style-2  ', 'placeholder':'  YYYY-MM-DD','required':'required'}),
			'date_project_end': forms.DateInput(format=('%d-%m-%Y'),attrs={'class':' input--style-2  ', 'placeholder':'  YYYY-MM-DD','required':'required'}),
			'is_PER_approved' : CheckboxInput(attrs={'type':'checkbox checker','required':'required','id':'checker',},  ),
			'is_PPWS_approved' : CheckboxInput(attrs={'type':'checkbox','required':'required',} ),
			'PER_date': forms.DateInput(format=('%d-%m-%Y'),attrs={'class':' input--style-2  answer', 'placeholder':'  YYYY-MM-DD','id':'answer'}),
			'PPWS_date': forms.DateInput(format=('%d-%m-%Y'),attrs={'class':' input--style-2   ', 'placeholder':'  YYYY-MM-DD'}),
			'alloted_trade' : TextInput(attrs={'class':'form-control', 'max_length':'30','required':'required'}),
			'alloted_trade_target' : NumberInput(attrs={'class':'form-control','required':'required'}),
			#'trade_target' : NumberInput(attrs={'class':'form-control input-sm','required':'required'}),
			#'tc_district' : TextInput(attrs={'class':'form-control input-sm', 'max_length':'150','required':'required'}),
			'mobilization_district' : TextInput(attrs={'class':'form-control', 'max_length':'150','required':'required'}),
			'mobilization_target' : NumberInput(attrs={'class':'form-control','required':'required'}),
			'project_id' : TextInput(attrs={'class':'form-control', 'max_length':'20','required':'required','readonly': 'readonly'}),
			'tlm_approved_status' : Select(attrs={'class':'select form-control',}, choices = tlm_Choices, ),
		}
