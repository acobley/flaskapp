import requests
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
    
    src = "http://" + IP_NGINX + "/mp4/bbb.mp4"
    
    return render_template('index.html', video_name=IP_NGINX, video_src=src)

@app.route('/Test/')
def hello_page():
    
    names = []
    for number in TEST:
        names.append( "<li> " +number+ " </li>" )
        
    return render_template('index.html', items="<li>"+TEST[4]+"</l1>")

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)