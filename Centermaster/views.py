from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from Centermaster.models import *
from project_master.models import *
from django.views import View
from django.core.files import File
import json
from django.core.files.temp import NamedTemporaryFile

def create_center(request):
	return render(request,'Center_Master/Form.html')


@csrf_exempt
def center_master_insert(request):
	# Normal Form Data###########################
	pia_name=request.POST.get('pia_name', False)
	Name_District=request.POST.get('Name_District', False)
	Assembly_Constituency=request.POST.get('Assembly_Constituency', False)
	Parliamentary_Constituency=request.POST.get('Parliamentary_Constituency', False)
	Name_of_training_Center=request.POST.get('Name_of_training_Center', False)
	Training_Centode_Alias=request.POST.get('Training_Centode_Alias', False)
	Address1_Training_Center=request.POST.get('Address1_Training_Center', False)
	Address2_Training_Center=request.POST.get('Address2_Training_Center', False)
	Mobile_No_TC_Manager=request.POST.get('Mobile_No_TC_Manager', False)
	Email_id_TC_Manager=request.POST.get('Email_id_TC_Manager', False)
	Distance_From_Bus_Stand=request.POST.get("Distance_From_Bus_Stand",False)
	Distance_From_Auto_Stand=request.POST.get('Distance_From_Auto_Stand', False)
	Distance_From_Railway_Station=request.POST.get('Distance_From_Railway_Station', False)
	Distance_From_Airport=request.POST.get('Distance_From_Airport', False)
	Latitude=request.POST.get('Latitude', False)
	Longituder=request.POST.get('Longitude', False)
	Photograph_Building_Sign=request.FILES.getlist('Photograph_Building_Sign')
	Photograph_adjoining_building=request.FILES.getlist('Photograph_adjoining_building')
	Ownership_of_the_Building=request.POST.get('Ownership_of_the_Building', False)
	Area_of_the_Building=request.POST.get('Area_of_the_Building', False)
	RCC=request.POST.get('RCC', False)
	Circulation_Area=request.POST.get('Circulation_Area', False)
	Open_space_Area=request.POST.get('Open_space_Area', False)
	Exlcusive_Bicycle_Parking=request.POST.get('Exlcusive_Bicycle_Parking', False)
	Open_Space_Security=request.POST.get('Open_Space_Security', False)
# Room Table Data ##############################################################################
	Rooms_Available_Number=request.POST.get('Rooms_Available_Number', False)
	Room_Length=request.POST.getlist('length_room', False)
	Room_Width=request.POST.getlist('width_room', False)
	Room_Area=request.POST.getlist('area_room', False)
	Roof_Height=request.POST.getlist('roof_height_room', False)
	Windows_Area=request.POST.getlist('windows_area_room', False)
#Corridor Table Data#######################################
	Number_Of_Corridor=request.POST.get('Number_Of_Corridor', False)
	Length_Of_Corridor=request.POST.getlist('length_corridor', False)
	Width_Of_Corridor=request.POST.getlist('width_corridor', False)
	Area_Of_Corridor=request.POST.getlist('area_corridor', False)
	Roof_Height_Corridor=request.POST.getlist('roof_height_corridor', False)
	Windows_Areas=request.POST.getlist('windows_area_corridor', False)
	Number_of_Lights=request.POST.getlist('lights_no_corridor', False)
	Number_Of_Fans=request.POST.getlist('fan no_corrdior', False)
	print(Length_Of_Corridor)
# Toilet Table Data##############################################################
	Number_Of_Toilets=request.POST.get('Number_Of_Toilets', False)
	Light_No=request.POST.getlist('lights_no', False)
	Lights_Image=request.FILES.getlist('light_image', False)
	Type_Flooring=request.POST.getlist('type_floor', False)
	Flooring_Image=request.FILES.getlist('floor_image', False)
	Connection_running_water=request.POST.getlist('connection_water', False)
	try:
		# Normal Data Save
		normal=Center_Master()
		normal.pia_name=pia_name
		normal.Name_District=Name_District
		normal.Assembly_Constituency=Assembly_Constituency
		normal.Parliamentary_Constituency=Parliamentary_Constituency
		normal.Name_of_training_Center=Name_of_training_Center
		normal.Training_Centode_Alias=Training_Centode_Alias
		normal.Address1_Training_Center=Address1_Training_Center
		normal.Address2_Training_Center=Address2_Training_Center
		normal.Mobile_No_TC_Manager=Mobile_No_TC_Manager
		normal.Email_id_TC_Manager=Email_id_TC_Manager
		normal.Distance_From_Bus_Stand=Distance_From_Bus_Stand
		normal.Distance_From_Auto_Stand=Distance_From_Auto_Stand
		normal.Distance_From_Railway_Station=Distance_From_Railway_Station
		normal.Distance_From_Airport=Distance_From_Airport
		normal.Latitude=Latitude
		normal.Longituder=Longituder
		for d in Photograph_Building_Sign:
			normal.Photograph_Building_Sign=File(d)
		for e in Photograph_adjoining_building:
			normal.Photograph_adjoining_building=File(e)
		# normal.Photograph_Building_Sign=File(Photograph_Building_Sign)
		# normal.Photograph_adjoining_building=File(Photograph_adjoining_building)
		normal.Ownership_of_the_Building=Ownership_of_the_Building
		normal.Area_of_the_Building=Area_of_the_Building
		normal.RCC=RCC
		normal.Circulation_Area=Circulation_Area
		normal.Open_space_Area=Open_space_Area
		normal.Exlcusive_Bicycle_Parking=Exlcusive_Bicycle_Parking
		normal.Open_Space_Security=Open_Space_Security
		normal.Rooms_Available_Number=Rooms_Available_Number
		normal.Number_Of_Corridor=Number_Of_Corridor
		normal.Number_Of_Toilets=Number_Of_Toilets
		normal.Project_id_id= Project_Master.objects.values_list('project_id', flat=True)[0]
		normal.save()
					

		# Room Table Data Save######################
		room_dict={}
		room_dict["Room_Length"]=Room_Length
		room_dict["Room_Width"]=Room_Width
		room_dict["Room_Area"]=Room_Area
		room_dict["Roof_Height"]=Roof_Height
		room_dict["Windows_Areas"]=Windows_Area
		number_room=len(Room_Area)
		for i in range(number_room):
			room=Roomtable()
			room.Room_Length=list(room_dict.values())[0][i]
			room.Room_Width=list(room_dict.values())[1][i]
			room.Room_Area=list(room_dict.values())[2][i]
			room.Roof_Height=list(room_dict.values())[3][i]
			room.Windows_Areas=list(room_dict.values())[4][i]
			room.save()


		#Corridor Table Data Save
		corridor_dict={}
		corridor_dict["Length_Of_Corridor"]=Length_Of_Corridor
		corridor_dict["Width_Of_Corridor"]=Width_Of_Corridor
		corridor_dict["Area_Of_Corridor"]=Area_Of_Corridor
		corridor_dict["Roof_Height_Corridor"]=Roof_Height_Corridor
		corridor_dict["Windows_Areas"]=Windows_Areas
		corridor_dict["Number_of_Lights"]=Number_of_Lights
		corridor_dict["Number_Of_Fans"]=Number_Of_Fans
		number_corridor=len(Length_Of_Corridor)
		for i in range(number_corridor):
			corridor=CorridorTable()
			corridor.Length_Of_Corridor=list(corridor_dict.values())[0][i]
			corridor.Width_Of_Corridor=list(corridor_dict.values())[1][i]
			corridor.Area_Of_Corridor=list(corridor_dict.values())[2][i]
			corridor.Roof_Height_Corridor=list(corridor_dict.values())[3][i]
			corridor.Windows_Areas=list(corridor_dict.values())[4][i]
			corridor.Number_of_Lights=list(corridor_dict.values())[5][i]
			corridor.Number_Of_Fans=list(corridor_dict.values())[6][i]
			corridor.save()
		# Toilet Table Data Save
		toilet_dict={}
		toilet_dict["Light_No"]=Light_No
		toilet_dict["Lights_Image"]=Lights_Image
		toilet_dict["Type_Flooring"]=Type_Flooring
		toilet_dict["Flooring_Image"]=Flooring_Image
		toilet_dict["Connection_running_water"]=Connection_running_water
		number_toilet=len(Light_No)
		for i in range(number_toilet):
			toilet=ToiletTable()
			toilet.Light_No=list(toilet_dict.values())[0][i]
			img_temp_Lights_Image=list(toilet_dict.values())[1][i]
			toilet.Type_Flooring=list(toilet_dict.values())[2][i]
			img_temp_Flooring_Image=list(toilet_dict.values())[3][i]
			toilet.Connection_running_water=list(toilet_dict.values())[4][i]
			toilet.Lights_Image=File(img_temp_Lights_Image)
			toilet.Flooring_Image=File(img_temp_Flooring_Image)
			toilet.save()
		response={"error":False,"errorMessage":"Updated Successfully"}
		return JsonResponse(response,safe=False)
	except:
		response={"error":True,"errorMessage":"Failed to Add Data"}
		return JsonResponse(response,safe=False)
