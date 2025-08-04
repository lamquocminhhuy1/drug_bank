#!/bin/bash

# Drug Interaction Tracker - VPS Deployment Script
# This script will install Docker, clone the repository, and deploy the application

set -e  # Exit on any error

echo "🚀 Starting Drug Interaction Tracker VPS Deployment..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
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

# Check if running as root or with sudo
if [[ $EUID -eq 0 ]]; then
    print_warning "Running as root. This is not recommended for security reasons."
fi

# Update system
print_status "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install required packages
print_status "Installing required packages..."
sudo apt install -y curl wget git ufw

# Install Docker
print_status "Installing Docker..."
if ! command -v docker &> /dev/null; then
    curl -fsSL https://get.docker.com -o get-docker.sh
    sudo sh get-docker.sh
    sudo usermod -aG docker $USER
    print_success "Docker installed successfully"
else
    print_success "Docker is already installed"
fi

# Install Docker Compose
print_status "Installing Docker Compose..."
if ! command -v docker-compose &> /dev/null; then
    sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    print_success "Docker Compose installed successfully"
else
    print_success "Docker Compose is already installed"
fi

# Start Docker service
print_status "Starting Docker service..."
sudo systemctl start docker
sudo systemctl enable docker

# Clone repository
print_status "Cloning repository..."
if [ -d "drug_bank" ]; then
    print_warning "Repository already exists. Updating..."
    cd drug_bank
    git pull
else
    git clone https://github.com/lamquocminhhuy1/drug_bank.git
    cd drug_bank
fi

# Create necessary directories with proper permissions
print_status "Creating directories and setting permissions..."
mkdir -p static staticfiles media
mkdir -p static/css static/js static/images

# Set proper ownership and permissions
sudo chown -R 1000:1000 static staticfiles media 2>/dev/null || true
sudo chmod -R 755 static staticfiles media

# Create database file with proper permissions
touch db.sqlite3
sudo chown 1000:1000 db.sqlite3 2>/dev/null || true
sudo chmod 644 db.sqlite3

# Clean up any existing containers
print_status "Cleaning up existing containers..."
docker-compose down 2>/dev/null || true
docker system prune -f 2>/dev/null || true

# Build and start application
print_status "Building and starting the application..."
docker-compose up --build -d

# Wait for application to be ready
print_status "Waiting for application to start..."
sleep 30

# Configure firewall
print_status "Configuring firewall..."
sudo ufw --force reset
sudo ufw allow ssh
sudo ufw allow 8001
sudo ufw allow 80
sudo ufw allow 443
sudo ufw --force enable

# Get VPS IP address
VPS_IP=$(curl -s ifconfig.me)

# Check if application is running
print_status "Checking application status..."
if curl -f http://localhost:8001/ > /dev/null 2>&1; then
    print_success "Application is running successfully!"
    echo ""
    echo "🎉 Deployment completed successfully!"
    echo ""
    echo "📱 Access your application:"
    echo "   🌐 Web Interface: http://$VPS_IP:8001/"
    echo "   📚 API Documentation: http://$VPS_IP:8001/api/swagger/"
    echo "   🛠️  Admin Panel: http://$VPS_IP:8001/admin/"
    echo "   🔌 API Root: http://$VPS_IP:8001/api/"
    echo ""
    echo "👤 Admin credentials:"
    echo "   Username: admin"
    echo "   Password: admin123456"
    echo ""
    echo "🔧 Management commands:"
    echo "   View logs: docker-compose logs -f"
    echo "   Stop app: docker-compose down"
    echo "   Restart: docker-compose up -d"
    echo "   Update: git pull && docker-compose up --build -d"
    echo "   Fix issues: ./fix_vps_issues.sh"
    echo ""
    echo "🔒 Firewall status:"
    sudo ufw status
    echo ""
    print_success "Your Drug Interaction Tracker is now live!"
else
    print_error "Application failed to start. Checking logs..."
    docker-compose logs --tail=20
    echo ""
    print_error "Deployment failed. Please check the logs above."
    echo ""
    print_status "Try running the fix script: ./fix_vps_issues.sh"
    exit 1
fi 