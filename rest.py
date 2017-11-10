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
    return render_template("ipapi.html/" + request.environ['REMOTE_ADDR'],ip=0,country=0,region=0,city=0,postal=0,latitude=0,longitude=0)

@app.route("/nasa")
def nasa():
    global info
    global dic
    api = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=Vs1fTIFQ7AQ7IsRUPbF91rL6DehZi1HQ36VwlsVW")
    info = json.loads(api.read())
    return render_template("base.html",image_url=info['url'],image_title=info['title'],explanation=info['explanation'])

if __name__ == "__main__":
    app.run()
