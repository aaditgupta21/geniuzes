# import "packages" from flask
from flask import Flask, render_template,request
from algorithm.image import image_data


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
def binary7():
    if request.form:
        bits = request.form.get("bits")
        if int(bits) >= 8:
            return render_template("binary-week7.html", bits=int(bits))
    return render_template("binary-week7.html", bits=8)

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

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
