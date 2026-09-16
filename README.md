# AI-Powered Smart Surveillance and Crime Detection System

## Project Overview
This project is an AI-based surveillance system that uses YOLOv8, OpenCV, and Streamlit to detect, track, and monitor people in video streams. The system identifies intrusions in restricted areas, generates alerts, stores logs, and provides a dashboard for monitoring.

## Features
- Person Detection using YOLOv8
- Person Tracking
- Restricted Zone Monitoring
- Intrusion Detection
- Screenshot Capture
- Event Logging (CSV)
- Dashboard Visualization
- Real-Time Video Processing

## Project Structure

```text
AI-Crime-Detection-System/
│
├── dashboard/
│   └── app.py
├── videos/
│   └── test.mp4
├── screenshots/
├── intrusion_detection.py
├── intrusion_log.csv
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Requirements

- Python 3.10 or higher
- OpenCV
- Ultralytics YOLOv8
- Pandas
- Streamlit

## Installation

### Step 1: Clone Repository

```bash
git clone https://github.com/dnshprjpt8000/AI-Crime-Detection-System.git
cd AI-Crime-Detection-System
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Project

### Run Intrusion Detection System

```bash
python intrusion_detection.py
```

### Run Dashboard

```bash
streamlit run dashboard/app.py
```

The dashboard will open in your browser at:

```text
http://localhost:8501
```

## How It Works

1. Video is captured and processed.
2. YOLOv8 detects people.
3. Tracking module assigns unique IDs.
4. Restricted zone is monitored.
5. Intrusion alerts are generated.
6. Events are stored in CSV logs.
7. Dashboard displays monitoring data.

## Screenshots

### Detection Output

[Insert Screenshot Here]

### Intrusion Alert

[Insert Screenshot Here]

### Dashboard

[Insert Screenshot Here]

## Future Enhancements

- Face Recognition
- Weapon Detection
- Email Alerts
- SMS Notifications
- Cloud Deployment
- Multi-Camera Support

## Author

Dinesh Prajapat