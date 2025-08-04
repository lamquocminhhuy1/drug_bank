# VPS Deployment Guide

Complete guide to deploy the Drug Interaction Tracker on your VPS.

## 🚀 **Quick Deploy (One Command)**

### Prerequisites
- Ubuntu/Debian VPS
- SSH access to your VPS
- Root or sudo access

### One-Command Deployment
```bash
# Run this on your VPS
curl -sSL https://raw.githubusercontent.com/lamquocminhhuy1/drug_bank/main/deploy_vps.sh | bash
```

## 🛠️ **Manual Deployment**

### Step 1: Update System
```bash
sudo apt update && sudo apt upgrade -y
```

### Step 2: Install Docker
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Logout and login again, or run:
newgrp docker
```

### Step 3: Clone Repository
```bash
# Clone the repository
git clone https://github.com/lamquocminhhuy1/drug_bank.git
cd drug_bank
```

### Step 4: Create Directories and Set Permissions
```bash
# Create necessary directories
mkdir -p static staticfiles media

# Set proper permissions
chmod 755 static staticfiles media

# Create database file with proper permissions
touch db.sqlite3
chmod 644 db.sqlite3

# Create static files structure
mkdir -p static/css static/js static/images
chmod -R 755 static
```

### Step 5: Build and Run Application
```bash
# Build and start the application
docker-compose up --build -d

# Wait for the application to be ready
sleep 30

# Check if the application is running
curl -f http://localhost:8001/ > /dev/null 2>&1 && echo "✅ Application is running!" || echo "❌ Application failed to start"
```

### Step 6: Configure Firewall
```bash
# Install UFW if not installed
sudo apt install ufw -y

# Allow SSH
sudo ufw allow ssh

# Allow web application port
sudo ufw allow 8001

# Allow HTTP and HTTPS (optional)
sudo ufw allow 80
sudo ufw allow 443

# Enable firewall
sudo ufw enable

# Check firewall status
sudo ufw status
```

## 🌐 **Access Your Application**

### Local Access
- **Web Interface**: http://localhost:8001/
- **API Documentation**: http://localhost:8001/api/swagger/
- **Admin Panel**: http://localhost:8001/admin/
- **API Root**: http://localhost:8001/api/

### External Access
Replace `YOUR_VPS_IP` with your actual VPS IP address:
- **Web Interface**: http://YOUR_VPS_IP:8001/
- **API Documentation**: http://YOUR_VPS_IP:8001/api/swagger/
- **Admin Panel**: http://YOUR_VPS_IP:8001/admin/
- **API Root**: http://YOUR_VPS_IP:8001/api/

### Admin Credentials
- **Username**: admin
- **Password**: admin123456

## 🔧 **Management Commands**

### View Logs
```bash
# View all logs
docker-compose logs -f

# View only web service logs
docker-compose logs -f web
```

### Stop Application
```bash
docker-compose down
```

### Restart Application
```bash
docker-compose up -d
```

### Rebuild and Restart
```bash
docker-compose up --build -d
```

### Update Application
```bash
# Pull latest changes
git pull

# Rebuild and restart
docker-compose up --build -d
```

## 🗄️ **Database Management**

### Backup Database
```bash
cp db.sqlite3 backup_$(date +%Y%m%d_%H%M%S).sqlite3
```

### Restore Database
```bash
cp backup.sqlite3 db.sqlite3
docker-compose restart
```

### Reset Database
```bash
rm db.sqlite3
docker-compose up --build -d
```

## 🔍 **Troubleshooting**

### Check Application Status
```bash
# Check if container is running
docker-compose ps

# Check container logs
docker-compose logs web

# Check if port is listening
netstat -tlnp | grep 8001
```

### Fix Common Issues

#### Permission Issues
```bash
# Fix permissions for database and static files
sudo chown -R 1000:1000 db.sqlite3 static staticfiles media
sudo chmod 644 db.sqlite3
sudo chmod -R 755 static staticfiles media
```

#### Port Already in Use
```bash
# Check what's using port 8001
sudo lsof -i :8001

# Kill process if needed
sudo kill -9 <PID>
```

#### Docker Issues
```bash
# Restart Docker service
sudo systemctl restart docker

# Clean up Docker
docker system prune -f
```

### Quick Fix Script
```bash
# Run the quick fix script
./fix_vps_issues.sh
```

## 📊 **Monitoring**

### Check Resource Usage
```bash
# Check Docker resource usage
docker stats

# Check disk usage
df -h

# Check memory usage
free -h
```

### Health Check
```bash
# Test application health
curl -f http://localhost:8001/api/stats/ && echo "✅ Application is healthy" || echo "❌ Application has issues"
```

## 🔒 **Security Considerations**

### Change Default Password
```bash
# Access Django shell
docker-compose exec web python manage.py shell

# Change admin password
from django.contrib.auth.models import User
user = User.objects.get(username='admin')
user.set_password('your-new-password')
user.save()
exit()
```

### Environment Variables
Create a `.env` file for production:
```bash
# Create .env file
cat > .env << EOF
DEBUG=False
SECRET_KEY=your-secure-secret-key-here
ALLOWED_HOSTS=your-vps-ip,your-domain.com
EOF
```

### SSL/HTTPS Setup (Optional)
```bash
# Install Nginx
sudo apt install nginx -y

# Configure Nginx as reverse proxy
sudo nano /etc/nginx/sites-available/drug-interaction

# Add configuration:
server {
    listen 80;
    server_name your-domain.com;
    
    location / {
        proxy_pass http://localhost:8001;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
    }
}

# Enable site
sudo ln -s /etc/nginx/sites-available/drug-interaction /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## 📝 **Complete Deployment Script**

Save this as `deploy_complete.sh`:

```bash
#!/bin/bash

echo "🚀 Deploying Drug Interaction Tracker..."

# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Clone repository
git clone https://github.com/lamquocminhhuy1/drug_bank.git
cd drug_bank

# Create directories and set permissions
mkdir -p static staticfiles media
chmod 755 static staticfiles media
touch db.sqlite3
chmod 644 db.sqlite3
mkdir -p static/css static/js static/images
chmod -R 755 static

# Build and start application
docker-compose up --build -d

# Wait for application
sleep 30

# Configure firewall
sudo apt install ufw -y
sudo ufw allow ssh
sudo ufw allow 8001
sudo ufw --force enable

# Check status
if curl -f http://localhost:8001/ > /dev/null 2>&1; then
    echo "✅ Deployment successful!"
    echo "🌐 Access your application at: http://$(curl -s ifconfig.me):8001/"
    echo "👤 Admin: admin / admin123456"
else
    echo "❌ Deployment failed. Check logs: docker-compose logs -f"
fi
```

Make it executable and run:
```bash
chmod +x deploy_complete.sh
./deploy_complete.sh
```

## 🎉 **Success!**

Your Drug Interaction Tracker is now running on your VPS!

- **Web Interface**: http://YOUR_VPS_IP:8001/
- **API Documentation**: http://YOUR_VPS_IP:8001/api/swagger/
- **Admin Panel**: http://YOUR_VPS_IP:8001/admin/

**Admin Login**: admin / admin123456 