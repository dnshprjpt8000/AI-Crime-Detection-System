from ultralytics import YOLO
import cv2
import csv
import os
from datetime import datetime

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open video
cap = cv2.VideoCapture("videos/test.mp4")

if not cap.isOpened():
    print("Video not found!")
    exit()

# Create screenshots folder
os.makedirs("screenshots", exist_ok=True)

# Restricted Zone Coordinates
ZONE_X1 = 300
ZONE_Y1 = 100
ZONE_X2 = 600
ZONE_Y2 = 400

# Store already logged IDs
logged_ids = set()

# Create CSV file if it doesn't exist
with open("intrusion_log.csv", "a", newline="") as file:
    writer = csv.writer(file)

    if file.tell() == 0:
        writer.writerow([
            "Time",
            "Person_ID",
            "Event"
        ])

while True:

    ret, frame = cap.read()

    if not ret:
        break

    results = model.track(
        frame,
        persist=True,
        classes=[0],      # Only persons
        verbose=False
    )

    annotated_frame = results[0].plot()

    # Draw Restricted Zone
    cv2.rectangle(
        annotated_frame,
        (ZONE_X1, ZONE_Y1),
        (ZONE_X2, ZONE_Y2),
        (0, 0, 255),
        3
    )

    cv2.putText(
        annotated_frame,
        "RESTRICTED ZONE",
        (ZONE_X1, ZONE_Y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 0, 255),
        2
    )

    boxes = results[0].boxes

    if boxes is not None:

        for box in boxes:

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            person_id = None

            if box.id is not None:
                person_id = int(box.id[0])

            # Draw center point
            cv2.circle(
                annotated_frame,
                (center_x, center_y),
                5,
                (255, 0, 0),
                -1
            )

            # Check Intrusion
            if (
                ZONE_X1 < center_x < ZONE_X2
                and
                ZONE_Y1 < center_y < ZONE_Y2
            ):

                cv2.putText(
                    annotated_frame,
                    "ALERT: INTRUSION DETECTED",
                    (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

                if (
                    person_id is not None
                    and
                    person_id not in logged_ids
                ):

                    logged_ids.add(person_id)

                    current_time = datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )

                    # Save Screenshot
                    screenshot_name = (
                        f"screenshots/person_{person_id}.jpg"
                    )

                    cv2.imwrite(
                        screenshot_name,
                        annotated_frame
                    )

                    # Save CSV Log
                    with open(
                        "intrusion_log.csv",
                        "a",
                        newline=""
                    ) as file:

                        writer = csv.writer(file)

                        writer.writerow([
                            current_time,
                            person_id,
                            "Intrusion"
                        ])

                    print(
                        f"[LOGGED] Person {person_id}"
                    )

    cv2.imshow(
        "AI Crime Detection System",
        annotated_frame
    )

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()