#!/bin/bash
set -e
cd "$(dirname "$0")"
echo "Starting Smart Security Camera..."
if [ -f orange-pi/requirements.txt ]; then
  python3 -m pip install -r orange-pi/requirements.txt --user || true
fi
python3 run.py
