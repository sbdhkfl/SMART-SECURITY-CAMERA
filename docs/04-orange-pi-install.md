# 04 - Orange Pi Installation

## Goal

Install the local application without requiring a cloud account or paid service.

## 1. Update the operating system

Use the normal package manager for the installed Armbian/Debian-based system.

## 2. Install system packages

The final installer will install Python, OpenCV dependencies, audio tools, SQLite, and service-management packages.

## 3. Create the application environment

The project will use a dedicated Python virtual environment. This keeps project packages separate from the operating system.

## 4. Copy configuration

Copy config/config.example.yaml to config/config.yaml and change the ESP32 camera stream URL.

Never commit config/config.yaml if it contains private addresses, passwords, or other secrets.

## 5. Start the development server

Run orange-pi/run.py during development. Production deployment will use a systemd service.

## 6. Test

Open the local health endpoint and run the camera check before enabling AI.

Detailed commands will be added after the exact ESP32-S3-CAM model is confirmed.
