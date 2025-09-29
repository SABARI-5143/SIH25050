import cv2
import os
import time
from ultralytics import YOLO

# Load YOLO model
model = YOLO("yolov8n.pt")

# Target classes
target_classes = ["car", "truck", "bus", "motorbike", "threewheel", "van"]
all_names = model.names
target_indices = [i for i, name in all_names.items() if name in target_classes]

# Save folder
save_folder = "detected_frames"
os.makedirs(save_folder, exist_ok=True)
frame_counter = 0

# Start webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cannot open camera")
    exit()

print("Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        continue

    # Run YOLO detection
    results = model(frame, classes=target_indices)
    annotated_frame = results[0].plot()

    # Show live annotated feed
    cv2.imshow("YOLO Live Feed", annotated_frame)

    # Save frames if detections exist
    if len(results[0].boxes) > 0:
        frame_counter += 1
        save_path = os.path.join(save_folder, f"frame_{frame_counter}.jpg")
        cv2.imwrite(save_path, annotated_frame)

    # Quit when "q" is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
