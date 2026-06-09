# Real-Time Object Detection — YOLOv8

**Overview**  
This project demonstrates real-time object detection using YOLOv8 (Ultralytics) and OpenCV. The app detects objects from a webcam, draws bounding boxes with labels/confidence, and displays FPS.

**Features**
- Real-time webcam inference using YOLOv8-n (small & fast)
- Annotated frames with class label and confidence
- FPS overlay for performance monitoring
- Optional Flask MJPEG streamer for web demos
- Easy to swap model weights (e.g., custom-trained `best.pt`)

**Tech stack**
- Python, OpenCV
- Ultralytics YOLOv8
- Flask (for demo stream)

**How to run**
1. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
