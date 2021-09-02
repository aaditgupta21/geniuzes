# import "packages" from flask
from flask import Flask, render_template,request

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")


@app.route('/aadit', methods=['GET', 'POST'])
def aadit():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:
            return render_template("aadit.html", name=name)
    return render_template("aadit.html", name="World")

@app.route('/adi', methods=['GET', 'POST'])
def adi():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("adi.html", nick=name)
    # starting and empty input default
    return render_template("adi.html", nick="World")

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

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
