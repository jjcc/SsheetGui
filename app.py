from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.debug = True



cattles = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'location': 'Toronto',
     'year': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'location': 'Ottawa',
     'year': '1973'},
]

options = {
    "minDimensions": [7, 5],
    "tableOverflow": True,
    "columns": [
        {"title": "Detailed Geographic Information", "width": 300, "type": "text"},
        {"title": "BC", "width": 100, "type": "numeric"},
        {"title": "SK", "width": 100, "type": "numeric"},
        {"title": "MB", "width": 100, "type": "numeric"},
        {"title": "ON", "width": 100, "type": "numeric"},
        {"title": "QC", "width": 100, "type": "numeric"},
        {"title": "Atlantic", "width": 100, "type": "numeric"}
    ]
}


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/api/v1/resources/cattles/all', methods=['GET'])
def api_all():
    return jsonify(cattles)


@app.route('/api/v1/resources/options', methods=['GET'])
def api_options():

    return jsonify(options)



if __name__ == '__main__':
    app.run()
