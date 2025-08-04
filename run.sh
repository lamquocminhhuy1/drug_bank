#!/bin/bash

# Drug Interaction Tracker - Simple Run Script
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
mkdir -p static staticfiles media

# Set proper permissions
echo "🔐 Setting proper permissions..."
chmod 755 static staticfiles media
chown -R 1000:1000 static staticfiles media 2>/dev/null || true

# Create database file with proper permissions
echo "💾 Creating database file..."
touch db.sqlite3
chmod 644 db.sqlite3
chown 1000:1000 db.sqlite3 2>/dev/null || true

# Create static files structure
echo "📁 Creating static files structure..."
mkdir -p static/css static/js static/images
chmod -R 755 static
chown -R 1000:1000 static 2>/dev/null || true

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
    echo "👤 Admin credentials:"
    echo "   Username: admin"
    echo "   Password: admin123456"
    echo ""
    echo "💾 Database: SQLite (db.sqlite3 file)"
    echo ""
    echo "🛑 To stop the application: docker-compose down"
    echo "🔄 To restart: docker-compose up -d"
    echo "📋 To view logs: docker-compose logs -f"
else
    echo "❌ Application failed to start. Check the logs:"
    echo "   docker-compose logs -f"
    exit 1
fi 