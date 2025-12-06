# app.py
from flask import Flask, Response, render_template_string
import cv2
from ultralytics import YOLO
import time

MODEL_NAME = "yolov8n.pt"
CONFIDENCE_THRESHOLD = 0.25
WEBCAM_ID = 0

app = Flask(__name__)
model = YOLO(MODEL_NAME)
model.conf = CONFIDENCE_THRESHOLD
cap = cv2.VideoCapture(WEBCAM_ID)

HTML_PAGE = """
<!doctype html>
<title>YOLOv8 Live Stream</title>
<h2>YOLOv8 - Real Time Object Detection</h2>
<img src="{{ url_for('video_feed') }}" width="800">
<p>Press Ctrl+C in terminal to stop the server.</p>
"""

def gen_frames():
    prev_time = 0
    while True:
        success, frame = cap.read()
        if not success:
            break
        results = model(frame)[0]
        annotated = results.plot()
        # Add FPS
        curr = time.time()
        fps = 1.0 / (curr - prev_time) if prev_time else 0.0
        prev_time = curr
        cv2.putText(annotated, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
        # Encode as JPEG
        ret, buffer = cv2.imencode('.jpg', annotated)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

@app.route('/')
def index():
    return render_template_string(HTML_PAGE)

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
