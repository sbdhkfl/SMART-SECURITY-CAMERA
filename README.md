# SMART-SECURITY-CAMERA

This is the smart security camera project we are building around the Orange Pi Zero 3 and ESP32-S3-CAM.

The main idea is simple: the camera sees something, the Orange Pi does the smart stuff locally, and you can check what is happening from the dashboard.

## What it can do
- Local face detection and face recognition
- Save more than 5 people, with the limit controlled by config
- Take a picture when an unknown person is detected
- Save event video when enabled
- Ask the unknown person who they are
- Record their answer with the USB microphone
- Keep the face, picture, video, and audio data on the local system
- Show the camera and events in a local dashboard
- Keep the main security features working without Internet
- Let you reach the system from outside your home through a secure private network
- Use open-source/local software instead of paid AI or cloud storage

## Hardware
1. Orange Pi Zero 3 2GB
2. ESP32-S3-CAM
3. Compatible camera sensor/lens
4. USB microphone
5. 64GB or larger microSD card
6. Stable power supplies
7. Wi-Fi/LAN router
8. Jumper wires and mounting hardware as needed

## How the whole thing works
Think of it like this:

**ESP32-S3-CAM -> camera video -> Orange Pi -> local AI -> face result -> event storage -> dashboard**

The ESP32-S3-CAM handles the camera side.

The Orange Pi is the main computer. It handles the AI, recordings, database, audio, dashboard, and network services.

## Remote access
When you are on the same network, the system works locally.

When you are somewhere else in the world, you need a secure network path back to your home. The project uses a VPN/private-network setup instead of putting the camera directly on the public Internet.

## Project rules
- Keep the important AI processing local
- Keep recordings and face data local
- Do not put passwords, tokens, or private keys in GitHub
- Keep the setup beginner-friendly
- Test each part before moving to the next part
- Keep the project open-source friendly

## Privacy
Face recognition and recording can be regulated depending on where you live. Use the system responsibly, follow local laws, and make sure people are properly informed when required.

## Documentation
The docs folder is where the full build guides, hardware list, wiring, setup, security, testing, backup, and troubleshooting steps go.

## Current status
The repository foundation and main architecture are set up. Next we build the actual camera firmware, local AI, face enrollment, unknown-person workflow, audio workflow, dashboard, remote access, and testing step by step.

## Run in VS Code
Open this repository in VS Code on the Orange Pi (or use VS Code Remote SSH). Run python run.py. Chrome opens automatically to the local security-camera dashboard. The ESP32-S3-CAM firmware and hardware setup remain separate so the browser interface does not complicate the hardware.
