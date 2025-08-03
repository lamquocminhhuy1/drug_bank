#!/bin/bash

# Drug Interaction Tracker - Auto Setup Script
echo "🚀 Setting up Drug Interaction Tracker..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are available"

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p media staticfiles

# Set proper permissions
echo "🔐 Setting proper permissions..."
chmod +x setup.sh

# Build and start the application
echo "🐳 Building and starting the application..."
docker-compose up --build -d

# Wait for the application to be ready
echo "⏳ Waiting for the application to be ready..."
sleep 30

# Check if the application is running
echo "🔍 Checking application status..."
if curl -f http://localhost:8001/ > /dev/null 2>&1; then
    echo "✅ Application is running successfully!"
    echo ""
    echo "🎉 Setup completed successfully!"
    echo ""
    echo "📱 Access your application:"
    echo "   🌐 Web Interface: http://localhost:8001/"
    echo "   📚 API Documentation: http://localhost:8001/api/swagger/"
    echo "   🛠️  Admin Panel: http://localhost:8001/admin/"
    echo "   🔌 API Root: http://localhost:8001/api/"
    echo ""
    echo "📊 Sample data has been loaded automatically."
    echo "👤 Admin credentials:"
    echo "   Username: admin"
    echo "   Password: (check the logs for auto-generated password)"
    echo ""
    echo "🛑 To stop the application: docker-compose down"
    echo "🔄 To restart: docker-compose up -d"
    echo "📋 To view logs: docker-compose logs -f"
else
    echo "❌ Application failed to start. Check the logs:"
    echo "   docker-compose logs -f"
    exit 1
fi 