from ultralytics import YOLO
import cv2

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open video
cap = cv2.VideoCapture("videos/test.mp4")

if not cap.isOpened():
    print("Video not found!")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Person counter
    person_count = 0

    # Run detection
    results = model(frame)

    for result in results:
        boxes = result.boxes

        for box in boxes:
            cls = int(box.cls[0])

            # Person class in COCO dataset
            if cls == 0:
                person_count += 1

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Draw bounding box
                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 255, 0),
                    2
                )

                # Label
                cv2.putText(
                    frame,
                    "Person",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

    # Show person count
    cv2.putText(
        frame,
        f"Persons: {person_count}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2
    )

    cv2.imshow("AI Crime Detection System", frame)

    # Press Q to quit
    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()