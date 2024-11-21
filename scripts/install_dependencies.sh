#!/bin/bash

# Script to install dependencies for the Data Visualizer tool

echo "============================================================"
echo "🚀 Starting Installation of Dependencies..."
echo "============================================================"

# Ensure Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python3 to continue."
    exit 1
fi

# Ensure pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Installing pip3..."
    sudo apt update && sudo apt install -y python3-pip
fi

# Install required Python packages
echo "Installing required Python libraries..."
pip3 install -r requirements.txt

# Confirm installation
if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
else
    echo "❌ Failed to install dependencies. Please check for errors."
    exit 1
fi

echo "============================================================"
echo "🎉 Installation Complete! You can now run the tool."
echo "============================================================"
