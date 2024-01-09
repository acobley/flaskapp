import requests
import json
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.debug = True

IP_DB = "34.16.159.36"
IP_NGINX = "34.125.25.53"

TEST = [
    1,2,3,4,5,6,7,8,9,10
]

@app.route('/')
def hello_world():
    
    URL_CATEGORIES = "http://34.16.159.36/myflix/categories"
    URL_VIDEOS = "http://34.16.159.36/myflix/videos"
    
    response = requests.get(URL_CATEGORIES)
    print(response)
    print(response.status_code)
    
    src = "http://" + IP_NGINX + "/mp4/bbb.mp4"
    
    return render_template('index.html', video_name=IP_NGINX, video_src=src)

@app.route('/Test/')
def hello_page():
    
    list = ""
    for item in TEST:
        list += "<li>" +str(item)+ "</li>\n"
        
    return render_template('index.html', items=list)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)