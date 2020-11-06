from flask import Flask
from flask import Response
import csv
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    emotionArr = []
    f = open('test.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        emotionArr.append(line)
    f.close()    
    return json.dumps(emotionArr)

if __name__ == '__main__':
    app.run()