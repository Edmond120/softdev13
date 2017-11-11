import urllib2
import json
from flask import Flask, render_template,request

app = Flask(__name__)

info = None


@app.route("/")
def root():
    return render_template("root.html")

@app.route("/ipapi")
def ipapi():
    print "=========="
    print request.environ['REMOTE_ADDR']
    if(request.environ['REMOTE_ADDR'] == "127.0.0.1"):
        info = json.loads(urllib2.urlopen("https://ipapi.co/json").read())
    else:
        info = json.loads(urllib2.urlopen("https://ipapi.co/" + request.environ['REMOTE_ADDR'] + "/json").read())
    return render_template("ipapi.html/",ip=info['ip'],country=info['country'],region=info['region'],city=info['city'],postal=info['postal'],latitude=info['latitude'],longitude=info['longitude'])

@app.route("/nasa")
def nasa():
    global info
    global dic
    api = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=Vs1fTIFQ7AQ7IsRUPbF91rL6DehZi1HQ36VwlsVW")
    info = json.loads(api.read())
    return render_template("base.html",image_url=info['url'],image_title=info['title'],explanation=info['explanation'])

if __name__ == "__main__":
    app.run()
