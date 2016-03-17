from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import json


def index(request):
    # path to .txt file containing path to .json
    # did this because .json path is different for two of my machines
    # will formalise later
    path = open('C:/Users/ZerongTony/OneDrive/PATH2JSON.txt').read()

    json_data = open(path+'notes.json')
    data = json.load(json_data)
    json_data.close()

    context = {
        'data': data
    }

    return render(request, 'index.html', context)
