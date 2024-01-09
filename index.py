import requests
import json
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# Custom modules
import modules.data.globals as glb

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_world():
    
    response = requests.get(glb.URL_CATEGORIES)    
    JSON_CATEGORIES = response.json()
    CATEGORIES = [item['category'] for item in JSON_CATEGORIES]
    
    list = ""
    for item in CATEGORIES:
        list += '<li><a class="dropdown-item" href="./">' +str(item).capitalize()+ '</li>\n'
    
    src = "http://" + glb.IP_NGINX + "/mp4/bbb.mp4"
    
    return render_template('index.html', video_name=glb.IP_NGINX, video_src=src, categories=list)

@app.route('/Test/')
def hello_page():

    
    response = requests.get(glb.URL_VIDEOS)
    print(response)
    JSON_VIDEOS = response.json()
    VIDEOS = [item['video']['Name'] for item in JSON_VIDEOS]
    
    list = ""
    for item in VIDEOS:
        list += "<li>" +str(item).capitalize()+ "</li>\n"
        
    return render_template('index.html', items=list)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)