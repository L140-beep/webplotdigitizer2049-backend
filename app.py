import matplotlib
matplotlib.use('Agg')
from flask import Flask, request
from flask_cors import CORS, cross_origin
import base64
import cv2
import numpy as np
import json
import plotdigitizer
import matplotlib.pyplot as plt

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'

@app.route('/', methods=["POST"])
@cross_origin()
def index():
    data = json.loads(request.data)
    decoded_data = base64.b64decode(data['image'])
    np_data = np.fromstring(decoded_data,np.uint8)
    color = data['color']
    dots = data['dots']
    graph_type = data['type']
    img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
    
    if(graph_type == 'line'):
        return json.dumps({"dataset" :plotdigitizer.line(img, color, dots)})
    elif(graph_type == 'points'):
        return json.dumps({"dataset" :plotdigitizer.points(img, color, dots)})
    elif(graph_type == 'line_filled'):
        return json.dumps({"dataset" :plotdigitizer.line_filled(img, color, dots)})
    elif(graph_type == 'barplot'):
        return json.dumps({"dataset" : plotdigitizer.barplot(img, color, dots)})
    else:
        return('NOT SUPPORTED')
@app.route('/', methods=["GET"])
def get():
    return("ok, the server is working, what's next?")

if (__name__ == '__main__'):
    app.run()
