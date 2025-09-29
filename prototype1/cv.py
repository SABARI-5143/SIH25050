from flask import Flask, Response, send_from_directory, jsonify
import cv2, os, threading, time
from ultralytics import YOLO
import numpy as np

app = Flask(__name__)

# Load YOLO
model = YOLO("yolov8n.pt")

# Target classes
target_classes = ["car", "truck", "bus", "motorbike", "threewheel", "van"]
all_names = model.names
target_indices = [i for i, name in all_names.items() if name in target_classes]

# Save folder
save_folder = "detected_frames"
os.makedirs(save_folder, exist_ok=True)
frame_counter = 0

# Shared frame storage
latest_frame = None
lock = threading.Lock()

# Start webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

# Detection loop
def detection_loop():
    global latest_frame, frame_counter
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        # Run YOLO detection
        results = model(frame, classes=target_indices)
        annotated_frame = results[0].plot()

        # Save the latest frame safely
        with lock:
            latest_frame = annotated_frame.copy()

        # Save detected frames
        if len(results[0].boxes) > 0:
            frame_counter += 1
            save_path = os.path.join(save_folder, f"frame_{frame_counter}.jpg")
            cv2.imwrite(save_path, annotated_frame)

        time.sleep(0.03)  # ~30 FPS

# Stream generator
def generate_stream():
    global latest_frame
    while True:
        with lock:
            if latest_frame is None:
                time.sleep(0.05)
                continue
            frame_copy = latest_frame.copy()

        ret, buffer = cv2.imencode('.jpg', frame_copy)
        if not ret:
            continue
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' +
               frame_bytes + b'\r\n')
        time.sleep(0.03)

# Flask routes
@app.route('/video')
def video():
    return Response(generate_stream(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/detected_frames/<filename>')
def serve_frame(filename):
    return send_from_directory(save_folder, filename)

@app.route('/dashboard_frames')
def dashboard_frames():
    frames = sorted(os.listdir(save_folder), reverse=True)[:8]
    return jsonify({"frames": [f"/detected_frames/{f}" for f in frames]})

if __name__ == "__main__":
    # Start detection in background
    t = threading.Thread(target=detection_loop, daemon=True)
    t.start()

    app.run(debug=True, threaded=True)
