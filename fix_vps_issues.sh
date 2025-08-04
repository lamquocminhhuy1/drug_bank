#!/bin/bash

# Drug Interaction Tracker - VPS Issues Fix Script
echo "🔧 Fixing VPS issues..."

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "❌ Please run as root (use sudo)"
    exit 1
fi

# Stop containers
echo "🛑 Stopping containers..."
docker-compose down

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p static staticfiles media

# Set proper permissions
echo "🔐 Setting proper permissions..."
chmod 755 static staticfiles media
chown -R 1000:1000 static staticfiles media

# Create empty database file if it doesn't exist
echo "💾 Creating database file..."
touch db.sqlite3
chmod 644 db.sqlite3
chown 1000:1000 db.sqlite3

# Create static files directory structure
echo "📁 Creating static files structure..."
mkdir -p static/css static/js static/images

# Set permissions for static files
chmod -R 755 static
chown -R 1000:1000 static

# Rebuild and start containers
echo "🐳 Rebuilding and starting containers..."
docker-compose up --build -d

# Wait for application to be ready
echo "⏳ Waiting for application to be ready..."
sleep 30

# Check if application is running
echo "🔍 Checking application status..."
if curl -f http://localhost:8001/ > /dev/null 2>&1; then
    echo "✅ Application is running successfully!"
    echo ""
    echo "🎉 Issues fixed successfully!"
    echo ""
    echo "📱 Access your application:"
    echo "   🌐 Web Interface: http://YOUR_VPS_IP:8001/"
    echo "   📚 API Documentation: http://YOUR_VPS_IP:8001/api/swagger/"
    echo "   🛠️  Admin Panel: http://YOUR_VPS_IP:8001/admin/"
    echo ""
    echo "👤 Admin credentials:"
    echo "   Username: admin"
    echo "   Password: admin123456"
else
    echo "❌ Application still has issues. Check the logs:"
    echo "   docker-compose logs -f"
    exit 1
fi 