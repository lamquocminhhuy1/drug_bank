#!/bin/bash

# Drug Interaction Tracker - Firewall Setup Script for Ubuntu VPS
echo "🔥 Setting up firewall for Drug Interaction Tracker..."

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "❌ Please run as root (use sudo)"
    exit 1
fi

# Update system
echo "📦 Updating system packages..."
apt update

# Install UFW if not installed
if ! command -v ufw &> /dev/null; then
    echo "📦 Installing UFW..."
    apt install ufw -y
fi

# Reset UFW to default
echo "🔄 Resetting UFW to default..."
ufw --force reset

# Enable UFW
echo "✅ Enabling UFW..."
ufw enable

# Allow SSH (IMPORTANT!)
echo "🔐 Allowing SSH access..."
ufw allow ssh
ufw allow 22

# Allow web application port
echo "🌐 Allowing web application port 8001..."
ufw allow 8001

# Allow HTTP and HTTPS (optional)
echo "🌐 Allowing HTTP and HTTPS..."
ufw allow 80
ufw allow 443

# Allow Docker ports (if needed)
echo "🐳 Allowing Docker ports..."
ufw allow 2375
ufw allow 2376

# Show firewall status
echo "📊 Firewall Status:"
ufw status verbose

echo ""
echo "🎉 Firewall setup completed!"
echo ""
echo "📱 Your application will be accessible at:"
echo "   🌐 Web Interface: http://YOUR_VPS_IP:8001/"
echo "   📚 API Documentation: http://YOUR_VPS_IP:8001/api/swagger/"
echo "   🛠️  Admin Panel: http://YOUR_VPS_IP:8001/admin/"
echo ""
echo "🔧 Useful commands:"
echo "   - Check firewall: sudo ufw status"
echo "   - Disable firewall: sudo ufw disable"
echo "   - Allow specific port: sudo ufw allow PORT"
echo "   - Deny specific port: sudo ufw deny PORT" 