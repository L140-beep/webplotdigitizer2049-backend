from flask import Flask, request
from flask_cors import CORS, cross_origin
import base64
import cv2
import numpy as np
import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'

@app.route('/', methods=["POST"])
@cross_origin()
def index():
    # decoded_data = base64.b64decode(img)
    # np_data = np.fromstring(decoded_data,np.uint8)
    # img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
    # cv2.imshow("test", img)
    # cv2.waitKey(0)
    # file = request.files.getlist("file")
    # image = base64.b64decode(request.data)
    # with open('image.txt', 'wb') as log:
    #     log.write(image)
    # json_data = json.loads(request.data)
    # print(json_data['image'])
    return 'hello, world!'   

if (__name__ == '__main__'):
    app.run()