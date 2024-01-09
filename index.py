import requests
import json
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
# from termcolor import colored

# Custom modules
import modules.data.globals as glb
import modules.utils.html_items as htmlItems
import modules.utils.logger as log

app = Flask(__name__)
app.debug = True

@app.route('/')
def index_page():
    
    response = requests.get(glb.URL_CATEGORIES)    
    if (response.status_code != 200):
        log.LOG_ERROR("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, JSON_CATEGORIES['Exception']['Message']))
        return log.cmd_color.RED + "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, JSON_CATEGORIES['Exception']['Message']) + log.cmd_color.WHITE
    else:
        log.LOG_SUCCESS("[{0}] -- Fetched correctly!".format(request.remote_addr))
        
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
    log.LOG_MESSAGE('['+request.remote_addr+'] --> ' + uuid)
    
    URL_UUID_FILTER = glb.URL_VIDEOS + '?filter={"video.uuid":"' +uuid+ '"}'
    response = requests.get(URL_UUID_FILTER)    
    if (response.status_code != 200):
        log.LOG_ERROR("Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, video['Exception']['Message']))
        return log.cmd_color.RED + "Unexpected response: {0}. Status: {1}. Message: {2}".format(response.reason, response.status, video['Exception']['Message']) + log.cmd_color.WHITE
    else:
        log.LOG_SUCCESS("[{0}] -- Fetched correctly!".format(request.remote_addr))
        
    JSON_VIDEO = response.json()
    VIDEO = JSON_VIDEO[0]['video']
    src = 'http://' + glb.IP_NGINX + '/mp4/' +  VIDEO['file']
    return render_template("video.html", video_name=VIDEO['Name'], pic=VIDEO['thumb'], video_src=src)

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