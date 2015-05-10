from flask import Flask, render_template, jsonify, json, request

application = Flask(__name__)
app = application

@app.route("/")
def index():
    return render_template("index.html")

# Routes for Visualizations

@app.route("/viz1")
def viz1():
# circle [small]
    return render_template("viz1.html")

@app.route("/viz2")
def viz2():
# circle [big]
    return render_template("viz2.html")

@app.route("/viz3")
def viz3():
# tree [small]
    return render_template("viz3.html")

@app.route("/viz4")
def viz4():
# tree [big]
    return render_template("viz4.html")


# Routes for Data

@app.route("/data")
def data():
    return jsonify(json.load(open('data.json')))

@app.route("/data_big")
def data_big():
    return jsonify(json.load(open('dataBig.json')))

@app.route("/data_small")
def data_small():
    return jsonify(json.load(open('dataSmall.json')))

# Get input from bowser

@app.route('/_trapClick')
def trapClick():
    clickName = request.args.get('target', 'empty', type=str)

    return jsonify(result = clickName)

if __name__ == "__main__":
    app.run(debug=True)
