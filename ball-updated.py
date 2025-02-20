import cv2
from ultralytics import YOLO

# Load YOLO model
model = YOLO('best.pt')

# Open video
video_path = 'video.MOV'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
if fps == 0 or fps is None:
    fps = 30  # Default FPS

# Define codec and output video
fourcc = cv2.VideoWriter_fourcc(*'avc1')  # Better for .mp4
output_video_path = 'output_video.mp4'
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_height, frame_width))  # Swap dimensions

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Rotate frame
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # Make predictions
    results = model(frame)

    # Filter soccer ball detections (class ID 2)
    filtered_boxes = [box for result in results for box in result.boxes if int(box.cls[0]) == 2]

    # Draw bounding boxes
    for box in filtered_boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        conf = box.conf[0].item()
        label = f"Soccer Ball {conf:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Show and save frame
    cv2.imshow("Soccer Ball Detection", frame)
    out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
