# app.py — Flask MJPEG streamer for browser-based demo
from flask import Flask, Response, render_template_string
import cv2
from ultralytics import YOLO
import time
from config import (
    MODEL_NAME, CONFIDENCE_THRESHOLD, WEBCAM_ID,
    FLASK_HOST, FLASK_PORT, STREAM_WIDTH
)

app = Flask(__name__)
model = YOLO(MODEL_NAME)
model.conf = CONFIDENCE_THRESHOLD
cap = cv2.VideoCapture(WEBCAM_ID)

HTML_PAGE = f"""
<!doctype html>
<html>
<head>
  <title>YOLOv8 Live Detection</title>
  <style>
    body {{ font-family: Arial, sans-serif; background: #111; color: #eee; text-align: center; padding: 20px; }}
    h2 {{ color: #00ff88; }}
    img {{ border: 2px solid #00ff88; border-radius: 8px; margin-top: 12px; }}
    p {{ color: #aaa; font-size: 13px; }}
  </style>
</head>
<body>
  <h2>YOLOv8 — Real-Time Object Detection</h2>
  <img src="{{{{ url_for('video_feed') }}}}" width="{STREAM_WIDTH}">
  <p>Press <kbd>Ctrl+C</kbd> in terminal to stop the server.</p>
</body>
</html>
"""

def gen_frames():
    prev_time = 0
    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)[0]
        annotated = results.plot()

        curr = time.time()
        fps = 1.0 / (curr - prev_time) if prev_time else 0.0
        prev_time = curr
        cv2.putText(annotated, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

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
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=False)