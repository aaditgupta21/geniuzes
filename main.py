# import "packages" from flask
from flask import Flask, render_template,request
from algorithm.image import image_data
import os
import requests
from api.webapi import api_bp


# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/aadit', methods=['GET', 'POST'])
def aadit():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("aadit.html", name=name)
    return render_template("aadit.html", name="World")
#adis route
@app.route('/adi', methods=['GET', 'POST'])
def adi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("adi.html", nick=name)
    # starting and empty input default
    return render_template("adi.html", nick="______")

@app.route('/rohit', methods=['GET', 'POST'])
def rohit():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("rohit.html", nick=name)
    # starting and empty input default
    return render_template("rohit.html", nick="there")

@app.route('/rohan', methods=['GET', 'POST'])
def rohan():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("rohan.html", name1=name)
    return render_template("rohan.html", name1="homie")

@app.route('/binary',methods=['GET', 'POST'])
def binary():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) >= 8:
            return render_template("binary.html", bits=int(bits))
    return render_template("binary.html", bits=8)

@app.route('/binaryweek7',methods=['GET', 'POST'])
def binaryweek7():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) >= 8:
            return render_template("binary-week7.html", bits=int(bits))
    return render_template("binary-week7.html", bits=8)

@app.route('/signedaddition',methods=['GET', 'POST'])
def signedaddition():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) >= 8:
            return render_template("signedaddition.html", bits=int(bits))
    return render_template("signedaddition.html", bits=8)


@app.route('/colorcodes',methods=['GET', 'POST'])
def colorcodes():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) >= 8:
            return render_template("colors.html", bits=int(bits))
    return render_template("colors.html", bits=8)

@app.route('/matchcolors',methods=['GET', 'POST'])
def matchcolors():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) >= 8:
            return render_template("matchcolors.html", bits=int(bits))
    return render_template("matchcolors.html", bits=8)


@app.route('/week0journal/')
def week0journal():
    return render_template("week0journal.html")

@app.route('/logicgate/')
def logicgate():
    return render_template("logicgate.html")


@app.route('/rgb/')
def rgb():
    rawList = image_data()
    colorList = []
    grayList = []
    for img in rawList:
        colorList.append(img['base64'])
        grayList.append(img['base64_GRAY'])
    return render_template('rgb.html', images=rawList, colored=colorList, grayed=grayList)


@app.route('/car', methods=['GET', 'POST'])
def car():
    url = "http://localhost:5000/api/car"
    response = requests.request("GET", url)
    return render_template("car.html", car=response.json())


@app.route('/cars', methods=['GET', 'POST'])
def cars():
    url = "http://localhost:5000/api/cars"
    response = requests.request("GET", url)
    return render_template("cars.html", cars=response.json())

@app.route('/mcolor', methods=['GET', 'POST'])
def mcolor():
    url = "http://localhost:5000/api/mcolor"
    response = requests.request("GET", url)
    if request.form:
        bits = request.form.get("bits")
        if int(bits) >= 8:
            return render_template("colors.html", bits=int(bits))
    return render_template("mcolor.html", mcolor=response.json(),  bits=8)

@app.route('/addition', methods=['GET', 'POST'])
def addition():
    url = "http://localhost:5000/api/addition"
    response = requests.request("GET", url)
    return render_template("addition.html", addition=response.json())

@app.route('/additions', methods=['GET', 'POST'])
def additions():
    url = "http://localhost:5000/api/additions"
    response = requests.request("GET", url)
    return render_template("additions.html", additions=response.json())

# @app.route('/createcolor', methods=['GET', 'POST'])
# def createcolor():
#     url = "http://localhost:5000/api/createcolor"
#     response = requests.request("GET", url)
#     return render_template("createcolor.html", createcolor=response.json())
#
# @app.route('/createcolors', methods=['GET', 'POST'])
# def createcolors():
#     url = "http://localhost:5000/api/createcolors"
#     response = requests.request("GET", url)
#     return render_template("createcolors.html", createcolors=response.json())


@app.route('/mcolors', methods=['GET', 'POST'])
def mcolors():
    url = "http://localhost:5000/api/mcolors"
    response = requests.request("GET", url)
    return render_template("mcolors.html", mcolors=response.json())

@app.route('/covid19', methods=['GET', 'POST'])
def covid19():
    url = "https://corona-virus-world-and-india-data.p.rapidapi.com/api"
    headers = {
        'x-rapidapi-key': "dec069b877msh0d9d0827664078cp1a18fajsn2afac35ae063",
        'x-rapidapi-host': "corona-virus-world-and-india-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    return render_template("covid19.html", stats=response.json())


@app.route('/newtoys')
def newtoys():
    return render_template("newtoys.html")

@app.route('/aboutus')
def aboutus():
    return render_template("aboutus.html")

@app.route('/signup')
def signup():
    return render_template("signup.html")

@app.route('/login')
def login():
    return render_template("login.html")


app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(
        debug=True,
        host="127.0.0.1",
        port=5000
    ),
