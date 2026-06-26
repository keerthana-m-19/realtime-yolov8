# Demo Instructions

## Prerequisites
- Python 3.9+
- A working webcam

## Setup

**1. Clone the repository**
```bash
git clone https://github.com/keerthana-m-19/realtime-yolov8.git
cd realtime-yolov8
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

> The YOLOv8 model weights (`yolov8n.pt`) are downloaded automatically on first run by Ultralytics.

---

## Running the Project

### Option A — Standalone Webcam Window
```bash
python yolo_realtime.py
```
- A window opens showing the live annotated feed.
- Press **`q`** to quit.

### Option B — Browser Stream (Flask)
```bash
python app.py
```
- Open your browser and go to: [http://localhost:5000](http://localhost:5000)
- Press **`Ctrl+C`** in the terminal to stop.

---

## Configuration

All settings are in `config.py`. No need to edit individual scripts:

| Setting | Default | Description |
|---|---|---|
| `MODEL_NAME` | `yolov8n.pt` | Model weights file |
| `CONFIDENCE_THRESHOLD` | `0.25` | Minimum confidence for detections |
| `WEBCAM_ID` | `0` | Camera index (try `1` for external cam) |
| `SAVE_OUTPUT` | `False` | Set `True` to record output video |
| `FLASK_PORT` | `5000` | Port for browser stream |

---

## Switching to a Custom Model

Replace `MODEL_NAME` in `config.py` with your trained weights:
```python
MODEL_NAME = "best.pt"   # your custom-trained model
```

---

## Troubleshooting

**Webcam not opening?**
- Make sure no other app is using it.
- Try changing `WEBCAM_ID` to `1` in `config.py`.

**Low FPS?**
- Switch to `yolov8n.pt` (smallest/fastest model).
- Reduce frame resolution in `yolo_realtime.py`.

**Module not found?**
- Make sure your virtual environment is activated.
- Re-run `pip install -r requirements.txt`.
