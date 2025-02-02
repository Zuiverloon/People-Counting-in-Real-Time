from flask import Flask, render_template, Response
import cv2
import sys
import numpy

app = Flask(__name__)

def get_frame():
    file="videos/output.mp4"
    #camera_port=0
    camera=cv2.VideoCapture(file)

    while True:
        retval, im = camera.read()
        imgencode=cv2.imencode('.jpg',im)[1]
        stringData=imgencode.tostring()
        yield (b'--frame\r\n'
            b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')


@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/video')
def vid():
     return Response(get_frame(),mimetype='multipart/x-mixed-replace; boundary=frame')




if __name__ == '__main__':
      app.run(host='0.0.0.0', port=8080)