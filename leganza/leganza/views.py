from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import leganza.musicDownloader

def main(request) :
    return render(request, 'main.html')
def calc(request) :
    return render(request, 'calc.html')
def result(request) :
    emotionArr = requests.get("http://localhost:5000").content
    emotionArr = json.loads(emotionArr)
    musicList = leganza.musicDownloader.getMusics(emotionArr[-8][0])
    return render(request, 'result.html', {'emotion' : json.dumps(emotionArr),'music' : json.dumps(musicList)})
def about(request) :
    return render(request, 'about.html')