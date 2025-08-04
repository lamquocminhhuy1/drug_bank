#!/bin/bash

# Drug Interaction Tracker - VPS Issues Fix Script
# This script fixes common permission and configuration issues

echo "🔧 Fixing VPS deployment issues..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Stop any running containers
print_status "Stopping running containers..."
docker-compose down 2>/dev/null || true

# Fix permissions for database and directories
print_status "Fixing permissions for database and directories..."

# Create directories if they don't exist
mkdir -p static staticfiles media
mkdir -p static/css static/js static/images

# Set proper ownership and permissions
sudo chown -R 1000:1000 static staticfiles media 2>/dev/null || true
sudo chmod -R 755 static staticfiles media

# Create database file with proper permissions
touch db.sqlite3
sudo chown 1000:1000 db.sqlite3 2>/dev/null || true
sudo chmod 644 db.sqlite3

# Fix Docker volume permissions
print_status "Fixing Docker volume permissions..."
sudo chown -R 1000:1000 . 2>/dev/null || true

# Clean up any existing containers and images
print_status "Cleaning up Docker environment..."
docker system prune -f 2>/dev/null || true
docker volume prune -f 2>/dev/null || true

# Rebuild and start the application
print_status "Rebuilding and starting the application..."
docker-compose up --build -d

# Wait for application to start
print_status "Waiting for application to start..."
sleep 30

# Check if application is running
print_status "Checking application status..."
if curl -f http://localhost:8001/ > /dev/null 2>&1; then
    print_success "Application is running successfully!"
    echo ""
    echo "🎉 Issues fixed successfully!"
    echo ""
    echo "📱 Access your application:"
    echo "   🌐 Web Interface: http://$(curl -s ifconfig.me):8001/"
    echo "   📚 API Documentation: http://$(curl -s ifconfig.me):8001/api/swagger/"
    echo "   🛠️  Admin Panel: http://$(curl -s ifconfig.me):8001/admin/"
    echo ""
    echo "👤 Admin: admin / admin123456"
else
    print_error "Application still has issues. Checking logs..."
    docker-compose logs --tail=20
    echo ""
    print_error "Please check the logs above for more details."
    exit 1
fi 