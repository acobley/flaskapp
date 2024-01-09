import requests
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
app.debug = True

IP_DB = "34.16.159.36"
IP_NGINX = "34.125.25.53"

TEST = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
        integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
   
    <link href="https://vjs.zencdn.net/8.9.0/video-js.css" rel="stylesheet" />
    <script src="https://vjs.zencdn.net/8.9.0/video.min.js"></script>

    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <title>myFlix</title>
</head>

<body>
    <a href="/"><h1>myFlix</h1></a>
    <a href="/Video/Big-Buck-Bunny"><p> Movie </p></a>

</body>

</html>
"""

@app.route('/')
def hello_world():
    
    src = "http://" + IP_NGINX + "/mp4/bbb.mp4"
    
    return render_template('index.html', video_name=IP_NGINX, video_src=src)

@app.route('/Test/')
def hello_page():
    
    return TEST

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80)