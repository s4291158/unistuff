from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.conf import settings
import json


def index(request):
    json_data = open('C:/Users/ZerongTony/OneDrive/notes.json')
    data = json.load(json_data)
    json_data.close()

    context = {
        'data': data
    }

    return render(request, 'index.html', context)
