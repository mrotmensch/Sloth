from flask import Flask, render_template, jsonify, json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

#Creates a route that will return the output of get_data() as a json
# aka you can go to http://localhost:5000/data and you will see the json
@app.route("/data")
def data():
    return jsonify(json.load(open('data.json')))

if __name__ == "__main__":
    app.run(debug=True)
