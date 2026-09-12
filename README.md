# AI-Powered Smart Surveillance & Crime Detection System

## Overview

This project is a Computer Vision based surveillance system that automatically detects, tracks, and monitors people in CCTV footage. The system identifies unauthorized entry into restricted areas and generates alerts with event logs and screenshots.

## Features

- Person Detection using YOLOv8
- Person Tracking with Unique IDs
- Person Counting
- Restricted Zone Monitoring
- Intrusion Detection Alerts
- Event Logging (CSV)
- Screenshot Capture
- Dashboard for Monitoring Intrusions

## Technologies Used

- Python
- OpenCV
- YOLOv8
- Streamlit
- Pandas

## Project Structure

```text
CrimeDetectionProject/
│
├── dashboard/
│   └── app.py
│
├── screenshots/
│
├── videos/
│
├── intrusion_detection.py
├── intrusion_log.csv
├── README.md
└── statement.md