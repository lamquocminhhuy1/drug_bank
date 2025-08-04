#!/bin/bash

# Drug Interaction Tracker - VPS Deployment Script
echo "🚀 Deploying Drug Interaction Tracker on VPS..."

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "❌ Please run as root (use sudo)"
    exit 1
fi

# Update system
echo "📦 Updating system packages..."
apt update && apt upgrade -y

# Install Docker if not installed
if ! command -v docker &> /dev/null; then
    echo "🐳 Installing Docker..."
    curl -fsSL https://get.docker.com -o get-docker.sh
    sh get-docker.sh
    usermod -aG docker $USER
    systemctl enable docker
    systemctl start docker
fi

# Install Docker Compose if not installed
if ! command -v docker-compose &> /dev/null; then
    echo "🐳 Installing Docker Compose..."
    curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
fi

# Install UFW if not installed
if ! command -v ufw &> /dev/null; then
    echo "🔥 Installing UFW firewall..."
    apt install ufw -y
fi

# Setup firewall
echo "🔥 Setting up firewall..."
ufw --force reset
ufw enable
ufw allow ssh
ufw allow 22
ufw allow 8001
ufw allow 80
ufw allow 443

# Clone repository
echo "📥 Cloning repository..."
cd /opt
git clone https://github.com/lamquocminhhuy1/drug_bank.git
cd drug_bank

# Create necessary directories
echo "📁 Creating directories..."
mkdir -p media staticfiles

# Set proper permissions
echo "🔐 Setting permissions..."
chmod +x setup.sh
chmod +x deploy_vps.sh

# Build and start application
echo "🐳 Building and starting application..."
docker-compose up --build -d

# Wait for application to be ready
echo "⏳ Waiting for application to be ready..."
sleep 30

# Get server IP
SERVER_IP=$(curl -s ifconfig.me)

# Check if application is running
echo "🔍 Checking application status..."
if curl -f http://localhost:8001/ > /dev/null 2>&1; then
    echo "✅ Application is running successfully!"
    echo ""
    echo "🎉 Deployment completed successfully!"
    echo ""
    echo "📱 Access your application:"
    echo "   🌐 Web Interface: http://$SERVER_IP:8001/"
    echo "   📚 API Documentation: http://$SERVER_IP:8001/api/swagger/"
    echo "   🛠️  Admin Panel: http://$SERVER_IP:8001/admin/"
    echo "   🔌 API Root: http://$SERVER_IP:8001/api/"
    echo ""
    echo "👤 Admin credentials:"
    echo "   Username: admin"
    echo "   Password: admin123456"
    echo ""
    echo "💾 Database: SQLite (db.sqlite3 file)"
    echo ""
    echo "🔧 Useful commands:"
    echo "   - View logs: docker-compose logs -f"
    echo "   - Stop app: docker-compose down"
    echo "   - Restart app: docker-compose up -d"
    echo "   - Check firewall: ufw status"
    echo ""
    echo "💡 Tips:"
    echo "   - Backup database: cp db.sqlite3 backup.sqlite3"
    echo "   - Restore database: cp backup.sqlite3 db.sqlite3"
    echo "   - Update app: git pull && docker-compose up --build -d"
else
    echo "❌ Application failed to start. Check the logs:"
    echo "   docker-compose logs -f"
    exit 1
fi 