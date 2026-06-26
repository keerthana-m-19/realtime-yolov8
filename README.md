# 🎯 Real-Time Object Detection — YOLOv8 + OpenCV

Real-time object detection from a live webcam using [YOLOv8](https://github.com/ultralytics/ultralytics) and OpenCV. Detects 80 COCO classes with bounding boxes, labels, confidence scores, and FPS overlay. Includes both a standalone desktop viewer and a browser-based Flask MJPEG stream.

---

## ✨ Features

- **Real-time webcam inference** using YOLOv8-n (fast & lightweight)
- **Annotated frames** — bounding boxes, class labels, confidence scores
- **FPS overlay** for live performance monitoring
- **Browser stream** via Flask MJPEG (open on any device on your network)
- **Centralized config** — change model, confidence, camera ID in one place
- **Custom model support** — swap in your own `best.pt` with one line

---

## 🗂️ Project Structure

```
realtime-yolov8/
├── config.py              ← all settings (model, camera, Flask port…)
├── yolo_realtime.py       ← standalone desktop webcam viewer
├── app.py                 ← Flask browser stream
├── requirements.txt       ← pinned dependencies
├── demo_instructions.md   ← detailed setup & usage guide
└── .gitignore
```

---

## ⚡ Quick Start

```bash
# 1. Clone
git clone https://github.com/keerthana-m-19/realtime-yolov8.git
cd realtime-yolov8

# 2. Install dependencies
pip install -r requirements.txt

# 3a. Run desktop viewer
python yolo_realtime.py

# 3b. Or run browser stream → open http://localhost:5000
python app.py
```

> Model weights (`yolov8n.pt`) are downloaded automatically on first run.

---

## ⚙️ Configuration

All settings live in `config.py` — no need to edit individual scripts:

| Setting | Default | Description |
|---|---|---|
| `MODEL_NAME` | `yolov8n.pt` | Weights file (nano = fastest) |
| `CONFIDENCE_THRESHOLD` | `0.25` | Min confidence for a detection |
| `WEBCAM_ID` | `0` | Camera index (try `1` for external) |
| `SAVE_OUTPUT` | `False` | Set `True` to record to `.mp4` |
| `FLASK_PORT` | `5000` | Browser stream port |

---

## 🔁 Using a Custom Model

```python
# config.py
MODEL_NAME = "best.pt"   # your custom-trained YOLOv8 weights
```

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **[Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)**
- **OpenCV** — video capture & rendering
- **Flask** — browser MJPEG stream
- **NumPy**

---

## 🚀 Future Improvements

- [ ] Object tracking (ByteTrack / DeepSORT integration)
- [ ] Multi-camera support
- [ ] Class filtering (detect only people / vehicles / etc.)
- [ ] Edge deployment (Raspberry Pi, Jetson Nano)
- [ ] REST API endpoint for detection results (JSON)

---

## 📄 License

[MIT](LICENSE)

---

## 👩‍💻 Author

**Keerthana M**  
B.Tech — Artificial Intelligence & Data Science  
Aspiring Machine Learning Engineer