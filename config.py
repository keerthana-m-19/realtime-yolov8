# config.py
# Central configuration for the YOLOv8 real-time detection project.
# Edit these values to customize behaviour without touching main scripts.

# ---------- Model ----------
MODEL_NAME = "yolov8n.pt"          # yolov8n / yolov8s / yolov8m / custom best.pt
CONFIDENCE_THRESHOLD = 0.25        # Detection confidence (0.0 – 1.0)

# ---------- Camera ----------
WEBCAM_ID = 0                      # 0 = default webcam, 1 = external camera

# ---------- Display ----------
SHOW_FPS = True                    # Overlay FPS counter on frames
WINDOW_NAME = "YOLOv8 - Real Time Object Detection"

# ---------- Output ----------
SAVE_OUTPUT = False                # Set True to save annotated video to disk
OUTPUT_FILE = "output_detected.mp4"

# ---------- Flask stream ----------
FLASK_HOST = "0.0.0.0"
FLASK_PORT = 5000
STREAM_WIDTH = 800                 # Display width in the browser (pixels)