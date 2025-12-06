# yolo_realtime.py
import time
import cv2
from ultralytics import YOLO

# ---- Settings ----
MODEL_NAME = "yolov8n.pt"   # small & fast; replace with yolov8s.pt or custom.pt if you train your own
CONFIDENCE_THRESHOLD = 0.25
WEBCAM_ID = 0               # change to 1 if external camera
WINDOW_NAME = "YOLOv8 - Real Time"
SHOW_FPS = True
SAVE_OUTPUT = False         # set True to save annotated output video
OUTPUT_FILE = "output_detected.mp4"
# -------------------

def main():
    # Load model
    print("Loading YOLOv8 model...")
    model = YOLO(MODEL_NAME)

    # Set model confidence
    model.conf = CONFIDENCE_THRESHOLD

    # Open webcam
    cap = cv2.VideoCapture(WEBCAM_ID)
    if not cap.isOpened():
        print(f"ERROR: Could not open webcam {WEBCAM_ID}")
        return

    # Prepare video writer if saving
    writer = None
    if SAVE_OUTPUT:
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        fps_est = cap.get(cv2.CAP_PROP_FPS) or 25.0
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        writer = cv2.VideoWriter(OUTPUT_FILE, fourcc, fps_est, (w, h))

    prev_time = 0

    print("Starting webcam. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("WARN: empty frame. Exiting.")
            break

        # Run detection (fast inference)
        # The model returns a Results object; index [0] gives the first result for this frame
        results = model(frame)[0]

        # results.plot() returns an annotated numpy array (BGR) with boxes & labels drawn
        annotated_frame = results.plot()  # Already in numpy BGR format for OpenCV

        # Compute FPS
        if SHOW_FPS:
            curr_time = time.time()
            fps = 1.0 / (curr_time - prev_time) if prev_time else 0.0
            prev_time = curr_time
            cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # Show frame
        cv2.imshow(WINDOW_NAME, annotated_frame)

        # Optionally save
        if writer is not None:
            writer.write(annotated_frame)

        # Quit on 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    if writer:
        writer.release()
    cv2.destroyAllWindows()
    print("Exited cleanly.")

if __name__ == "__main__":
    main()
