#!/bin/bash

# Script to run the Data Visualizer tool

echo "============================================================"
echo "🚀 Launching Data Visualizer with ASCII Charts"
echo "============================================================"

# Ensure Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 is not installed. Please install Python3 to continue."
    exit 1
fi

# Run the main Python script
python3 src/main.py

if [ $? -eq 0 ]; then
    echo "✅ Program exited successfully."
else
    echo "❌ Program encountered an error. Check logs for details."
    exit 1
fi

echo "============================================================"
echo "🎉 Thank you for using the Data Visualizer!"
echo "============================================================"
