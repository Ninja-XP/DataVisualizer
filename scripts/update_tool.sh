#!/bin/bash

# Script to update the Data Visualizer tool

echo "============================================================"
echo "🚀 Updating Data Visualizer Tool"
echo "============================================================"

# Check if Git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git to update the tool."
    exit 1
fi

# Pull latest changes from GitHub
echo "Fetching the latest updates from the repository..."
git pull origin main

# Check if the pull was successful
if [ $? -eq 0 ]; then
    echo "✅ Tool updated successfully!"
else
    echo "❌ Update failed. Please check your Git setup or repository access."
    exit 1
fi

# Reinstall dependencies (if necessary)
echo "Reinstalling dependencies to ensure compatibility..."
bash scripts/install_dependencies.sh

echo "============================================================"
echo "🎉 Update Complete! You are now on the latest version."
echo "============================================================"
