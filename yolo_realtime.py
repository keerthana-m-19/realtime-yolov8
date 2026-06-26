# yolo_realtime.py
import time
import cv2
from ultralytics import YOLO
from config import (
    MODEL_NAME, CONFIDENCE_THRESHOLD, WEBCAM_ID,
    WINDOW_NAME, SHOW_FPS, SAVE_OUTPUT, OUTPUT_FILE
)

def main():
    print("Loading YOLOv8 model...")
    model = YOLO(MODEL_NAME)
    model.conf = CONFIDENCE_THRESHOLD

    cap = cv2.VideoCapture(WEBCAM_ID)
    if not cap.isOpened():
        print(f"ERROR: Could not open webcam {WEBCAM_ID}")
        return

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
            print("WARN: Empty frame. Exiting.")
            break

        results = model(frame)[0]
        annotated_frame = results.plot()

        if SHOW_FPS:
            curr_time = time.time()
            fps = 1.0 / (curr_time - prev_time) if prev_time else 0.0
            prev_time = curr_time
            cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        cv2.imshow(WINDOW_NAME, annotated_frame)

        if writer is not None:
            writer.write(annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    if writer:
        writer.release()
    cv2.destroyAllWindows()
    print("Exited cleanly.")

if __name__ == "__main__":
    main()