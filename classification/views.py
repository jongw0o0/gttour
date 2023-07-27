from django.shortcuts import render
import json

def index(request):
    similadest_file_path = './similadest.json'
    destination_file_path = './destination.json'

    with open(similadest_file_path, 'r', encoding='utf-8') as json_file:
        similadest_data = json.load(json_file)
    with open(destination_file_path, 'r', encoding='utf-8') as json_file:
        destination_data = json.load(json_file)


    data = {
        'destination_data': destination_data,
        'similadest_data': similadest_data,
    }

    return render(request, 'classification/classification.html', {'data': data})