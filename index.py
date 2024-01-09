import requests
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.debug = True

IP_DB = "34.16.159.36"
IP_NGINX = "34.125.25.53"

@app.route('/')
def hello_world():
    
    src = "http://" + IP_NGINX + "/mp4/bbb.mp4"
    
    return render_template('index.html', video_name=IP_NGINX, video_src=src)

@app.route('/Video/<name>')
def hello_page(name):
    return '<h1>Hello '+name+'</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)