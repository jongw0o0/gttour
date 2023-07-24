from django.shortcuts import render
from .models import Tourmodel
# from classification.views import index
import csv
import json

def similadest_view(request):
    with open('./similadest.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        similadest_data = list(csv_reader)
    print('5',similadest_data)
    similadest_data_list = []  
    for json_value in similadest_data:
        location = json_value[0]    
        try:
            db_object = Tourmodel.objects.get(location=location)
            similadest_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative' : db_object.negative,
                'image': db_object.image.url, 
                'tour_loc': db_object.tour_loc,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('similadest_data_list.json', 'w') as json_file:
        json.dump(similadest_data_list, json_file)
    print('6',similadest_data_list)
    return render(request, 'tourlist/similadest.html', {'similadest_data_list': similadest_data_list})


def destination_view(request):
    with open('./destination.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        destination_data = list(csv_reader)
    destination_data_list = []  
    for json_value in destination_data:
        location = json_value[0]    

        try:
            db_object = Tourmodel.objects.get(location=location)
            destination_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative' : db_object.negative,
                'image': db_object.image.url, 
                'tour_loc': db_object.tour_loc,
                'url': f'/tourlist/destination_view/{db_object.location}/'
            })
        except Tourmodel.DoesNotExist:
            pass

    with open('destination_data_list.json', 'w') as json_file:
        json.dump(destination_data_list, json_file)
    print('7',destination_data_list)
    return render(request, 'tourlist/destination.html', {'destination_data_list': destination_data_list})






def simlist1(request):
    with open('./similadest.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        similadest_data = list(csv_reader)
    print('5',similadest_data)
    similadest_data_list = []  
    for json_value in similadest_data:
        location = json_value[0]    
        try:
            db_object = Tourmodel.objects.get(location=location)
            similadest_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative' : db_object.negative,
                'image': db_object.image.url, 
                'tour_loc': db_object.tour_loc,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('similadest_data_list.json', 'w') as json_file:
        json.dump(similadest_data_list, json_file)
    print('6',similadest_data_list)
    return render(request, 'tourlist/simlist1.html', {'similadest_data_list': similadest_data_list})

def simlist2(request):
    with open('./similadest.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        similadest_data = list(csv_reader)
    print('5',similadest_data)
    similadest_data_list = []  
    for json_value in similadest_data:
        location = json_value[0]    
        try:
            db_object = Tourmodel.objects.get(location=location)
            similadest_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative' : db_object.negative,
                'image': db_object.image.url, 
                'tour_loc': db_object.tour_loc,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('similadest_data_list.json', 'w') as json_file:
        json.dump(similadest_data_list, json_file)
    print('6',similadest_data_list)
    return render(request, 'tourlist/simlist1.html', {'similadest_data_list': similadest_data_list})

def simlist3(request):
    with open('./similadest.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        similadest_data = list(csv_reader)
    print('5',similadest_data)
    similadest_data_list = []  
    for json_value in similadest_data:
        location = json_value[0]    
        try:
            db_object = Tourmodel.objects.get(location=location)
            similadest_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative' : db_object.negative,
                'image': db_object.image.url, 
                'tour_loc': db_object.tour_loc,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('similadest_data_list.json', 'w') as json_file:
        json.dump(similadest_data_list, json_file)
    print('6',similadest_data_list)
    return render(request, 'tourlist/simlist1.html', {'similadest_data_list': similadest_data_list})

def simlist4(request):
    with open('./similadest.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        similadest_data = list(csv_reader)
    print('5',similadest_data)
    similadest_data_list = []  
    for json_value in similadest_data:
        location = json_value[0]    
        try:
            db_object = Tourmodel.objects.get(location=location)
            similadest_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative' : db_object.negative,
                'image': db_object.image.url, 
                'tour_loc': db_object.tour_loc,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('similadest_data_list.json', 'w') as json_file:
        json.dump(similadest_data_list, json_file)
    print('6',similadest_data_list)
    return render(request, 'tourlist/simlist1.html', {'similadest_data_list': similadest_data_list})

def simlist5(request):
    with open('./similadest.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        similadest_data = list(csv_reader)
    print('5',similadest_data)
    similadest_data_list = []  
    for json_value in similadest_data:
        location = json_value[0]    
        try:
            db_object = Tourmodel.objects.get(location=location)
            similadest_data_list.append({
                'location': db_object.location,
                'positive': db_object.positive,
                'negative' : db_object.negative,
                'image': db_object.image.url, 
                'tour_loc': db_object.tour_loc,
            })
        except Tourmodel.DoesNotExist:
            pass
        
    with open('similadest_data_list.json', 'w') as json_file:
        json.dump(similadest_data_list, json_file)
    print('6',similadest_data_list)
    return render(request, 'tourlist/simlist1.html', {'similadest_data_list': similadest_data_list})