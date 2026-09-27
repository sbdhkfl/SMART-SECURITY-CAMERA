# 07 - No-Internet Operation

The core system must continue to work after Internet access is removed.

## Expected to keep working
- camera stream on the local network
- face detection
- face recognition
- snapshots
- local video recording
- USB microphone recording
- local voice prompt
- local database
- local dashboard

## Expected not to work
- remote viewing from outside the home
- downloading operating-system updates
- downloading model files that have not already been installed

Test offline operation by disconnecting the Internet while keeping the Orange Pi and ESP32 on the same LAN.
