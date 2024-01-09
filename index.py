import requests
import json
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from termcolor import colored

# Custom modules
import modules.data.globals as glb
import modules.utils.html_items as htmlItems

app = Flask(__name__)
app.debug = True

@app.route('/')
def index_page():
    
    response = requests.get(glb.URL_CATEGORIES)    
    JSON_CATEGORIES = response.json()
    CATEGORIES = [item['category'] for item in JSON_CATEGORIES]
    
    list = ""
    for item in CATEGORIES:
        list += '<li><a class="dropdown-item" href="./">' +str(item).capitalize()+ '</a></li>\n'
    
    src = "http://" + glb.IP_NGINX + "/pics/bbb-th.png"
    
    card = htmlItems.column_card("Big Bug Bunny", "380613d5-71b3-4f24-8a58-ca1a260b49d3", "http://34.125.25.53/pics/bbb-th.png")
    
    return render_template('index.html', categories=list, video_cards=card)

@app.route('/Videos/<uuid>')
def video_page(uuid):
    
    print(colored(request.remote_addr + ' - ' + uuid, 'cyan'))
    return uuid

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