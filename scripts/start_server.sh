#!/bin/bash

# This script starts the Flask server for the Raspberry Pi Wi-Fi Setup

# Navigate to the src directory
cd src

# Install Python dependencies
pip3 install -r requirements.txt

# Run the Flask application
sudo python3 main.py
