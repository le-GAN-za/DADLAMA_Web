from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
def main(request) :
    return render(request, 'main.html')
def calc(request) :
    return render(request, 'calc.html')
def result(request) :
    emotionArr = requests.get("http://localhost:5000").content
    emotionArr = json.loads(emotionArr)
    return render(request, 'result.html', {'emotion' : emotionArr})
def about(request) :
    return render(request, 'about.html')