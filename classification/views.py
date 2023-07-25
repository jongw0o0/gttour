from django.http import JsonResponse
from django.shortcuts import render
import csv
import json
import urllib.request
# from tourlist.views import similadest_view, destination_view, total_view

def index(request):
    csv_file_path_destination = './destination.csv'
    csv_file_path_similadest = './similadest.csv'

    with open(csv_file_path_similadest, 'r',  encoding='cp949') as csvfile:
        csv_reader = csv.reader(csvfile)
        similadest_data = list(csv_reader)
        with open('similadest_data.json', 'w', encoding='cp949') as json_file:
            json.dump(similadest_data, json_file)

    with open(csv_file_path_destination, 'r', encoding='cp949') as csvfile:
        csv_reader = csv.reader(csvfile)
        destination_data = list(csv_reader)
        with open('destination_data.json', 'w', encoding='cp949') as json_file:
            json.dump(destination_data, json_file)


    print('1',destination_data,'2',similadest_data) # 콘솔 확인용

    data = {
        'destination_data': destination_data,
        'similadest_data': similadest_data,
    }

    return render(request, 'classification/classification.html', {'data': data})