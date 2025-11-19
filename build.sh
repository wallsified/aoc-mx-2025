#!/bin/bash
set -e

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

rm -rf public
mkdir -p public

reflex init
reflex export

# Check if zip files exist before unzipping
if [ -f "frontend.zip" ]; then
    unzip -o frontend.zip -d public
    rm -f frontend.zip
else
    echo "Error: frontend.zip not found"
    exit 1
fi

deactivate