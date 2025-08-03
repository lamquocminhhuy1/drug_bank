#!/bin/bash

echo "Testing Docker deployment for Drug Interaction Tracker"
echo "====================================================="

# Build the Docker image
echo "Building Docker image..."
docker build -t drug-interaction-tracker .

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully"
else
    echo "❌ Docker build failed"
    exit 1
fi

# Test running the container
echo "Testing container startup..."
docker run -d --name test-drug-app -p 8002:8001 drug-interaction-tracker

# Wait for container to start
sleep 10

# Test if the application is responding
echo "Testing application response..."
response=$(curl -s -o /dev/null -w "%{http_code}" http://localhost:8002/)

if [ "$response" = "200" ]; then
    echo "✅ Application is running successfully on port 8002"
    echo "🌐 Web Interface: http://localhost:8002"
    echo "🔌 API Endpoint: http://localhost:8002/api/"
else
    echo "❌ Application failed to start properly"
fi

# Clean up test container
echo "Cleaning up test container..."
docker stop test-drug-app
docker rm test-drug-app

echo "Docker test completed!" 