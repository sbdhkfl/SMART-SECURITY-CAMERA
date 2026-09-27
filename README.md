# SMART-SECURITY-CAMERA

A local-first smart security camera built around an Orange Pi Zero 3 and ESP32-S3-CAM.

## Goals
- Local face detection and recognition.
- More than five enrolled people; the limit is configuration-driven.
- Unknown-person snapshots and configurable video/event recording.
- USB microphone recording and a local voice-response workflow.
- Local dashboard and live video.
- Core detection, recording, and recognition continue without Internet.
- Remote live viewing through a secure private network/VPN layer; AI and stored data remain on the user's hardware.
- No paid AI APIs and no cloud AI/storage.
- Open-source, documented, testable, and beginner-friendly.

## Hardware
1. Orange Pi Zero 3 (2 GB)
2. ESP32-S3-CAM
3. USB microphone
4. Storage suitable for the operating system and event retention
5. Network connection for remote access only

## Architecture
ESP32-S3-CAM -> local camera stream -> Orange Pi Zero 3 -> detection/recognition -> event database + media storage -> local web dashboard.

## Important networking rule
Core security functions do not depend on cloud services. Remote viewing from outside the home necessarily needs an Internet path. The design uses a VPN/private-network layer rather than exposing the camera service directly to the public Internet.

## Documentation
See the docs directory for the complete build, wiring, installation, security, testing, backup, and troubleshooting guides.

## Privacy
Face recognition and recording can be legally regulated depending on where the system is used. Obtain appropriate consent and follow applicable laws. Do not use this project for covert surveillance.

## Status
Phase 1: repository foundation and architecture.
