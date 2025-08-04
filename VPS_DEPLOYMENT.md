# VPS Deployment Guide - Drug Interaction Tracker

## 🚀 **One-Command Deployment (Recommended)**

### **Bước 1: SSH vào VPS**
```bash
ssh root@YOUR_VPS_IP
```

### **Bước 2: Download và chạy deployment script**
```bash
# Download script
wget https://raw.githubusercontent.com/lamquocminhhuy1/drug_bank/main/deploy_vps.sh

# Chạy script với quyền root
sudo bash deploy_vps.sh
```

## 🔧 **Manual Deployment**

### **Bước 1: Cài đặt Docker**
```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
sudo systemctl enable docker
sudo systemctl start docker

# Install Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

### **Bước 2: Cấu hình Firewall**
```bash
# Install UFW
sudo apt install ufw -y

# Setup firewall
sudo ufw --force reset
sudo ufw enable
sudo ufw allow ssh
sudo ufw allow 22
sudo ufw allow 8001
sudo ufw allow 80
sudo ufw allow 443

# Check status
sudo ufw status verbose
```

### **Bước 3: Deploy Application**
```bash
# Clone repository
cd /opt
sudo git clone https://github.com/lamquocminhhuy1/drug_bank.git
cd drug_bank

# Create directories
sudo mkdir -p media staticfiles

# Build and start
sudo docker-compose up --build -d

# Check status
sudo docker-compose ps
```

## 📱 **Access Application**

### **Get VPS IP Address**
```bash
# Method 1: Using curl
curl -s ifconfig.me

# Method 2: Using hostname
hostname -I

# Method 3: Using ip command
ip addr show
```

### **Access URLs**
- **Web Interface**: `http://YOUR_VPS_IP:8001/`
- **API Documentation**: `http://YOUR_VPS_IP:8001/api/swagger/`
- **Admin Panel**: `http://YOUR_VPS_IP:8001/admin/`
- **API Root**: `http://YOUR_VPS_IP:8001/api/`

### **Admin Credentials**
- **Username**: `admin`
- **Password**: `admin123456`

## 🔧 **Management Commands**

### **Application Management**
```bash
# View logs
sudo docker-compose logs -f

# Stop application
sudo docker-compose down

# Restart application
sudo docker-compose up -d

# Rebuild and restart
sudo docker-compose up --build -d

# Check status
sudo docker-compose ps
```

### **Database Management**
```bash
# Backup database
sudo cp db.sqlite3 backup.sqlite3

# Restore database
sudo cp backup.sqlite3 db.sqlite3

# Reset database (will lose all data)
sudo rm db.sqlite3
sudo docker-compose up --build -d
```

### **Firewall Management**
```bash
# Check firewall status
sudo ufw status

# Allow specific port
sudo ufw allow PORT_NUMBER

# Deny specific port
sudo ufw deny PORT_NUMBER

# Disable firewall (not recommended)
sudo ufw disable
```

## 🔍 **Troubleshooting**

### **Port 8001 not accessible**
```bash
# Check if port is open
sudo netstat -tlnp | grep 8001

# Check firewall
sudo ufw status

# Allow port manually
sudo ufw allow 8001
```

### **Application not starting**
```bash
# Check logs
sudo docker-compose logs -f

# Check container status
sudo docker-compose ps

# Restart containers
sudo docker-compose restart
```

### **Database issues**
```bash
# Check database file
ls -la db.sqlite3

# Fix permissions
sudo chown 1000:1000 db.sqlite3
sudo chmod 644 db.sqlite3
```

### **Docker issues**
```bash
# Restart Docker service
sudo systemctl restart docker

# Check Docker status
sudo systemctl status docker

# Clean up Docker
sudo docker system prune -a
```

## 🔒 **Security Recommendations**

### **1. Change Default Admin Password**
```bash
# Access admin panel
# Go to: http://YOUR_VPS_IP:8001/admin/
# Login with: admin/admin123456
# Change password in User Management
```

### **2. Use HTTPS (Optional)**
```bash
# Install Certbot
sudo apt install certbot -y

# Get SSL certificate
sudo certbot certonly --standalone -d your-domain.com
```

### **3. Regular Backups**
```bash
# Create backup script
cat > /opt/backup.sh << 'EOF'
#!/bin/bash
cd /opt/drug_bank
cp db.sqlite3 backup_$(date +%Y%m%d_%H%M%S).sqlite3
echo "Backup created: backup_$(date +%Y%m%d_%H%M%S).sqlite3"
EOF

chmod +x /opt/backup.sh

# Add to crontab (daily backup at 2 AM)
echo "0 2 * * * /opt/backup.sh" | sudo crontab -
```

## 📊 **Monitoring**

### **Check Application Health**
```bash
# Test web interface
curl -I http://localhost:8001/

# Test API
curl -I http://localhost:8001/api/

# Check database
sudo docker-compose exec web python manage.py dbshell
```

### **System Resources**
```bash
# Check disk usage
df -h

# Check memory usage
free -h

# Check CPU usage
top

# Check Docker resources
sudo docker stats
```

## 🎉 **Success Indicators**

✅ **Application running**: `http://YOUR_VPS_IP:8001/` loads successfully
✅ **API working**: `http://YOUR_VPS_IP:8001/api/` returns JSON
✅ **Admin accessible**: `http://YOUR_VPS_IP:8001/admin/` shows login page
✅ **Firewall active**: `sudo ufw status` shows enabled
✅ **Docker running**: `sudo docker-compose ps` shows containers up

## 📞 **Support**

If you encounter issues:
1. Check logs: `sudo docker-compose logs -f`
2. Check firewall: `sudo ufw status`
3. Check Docker: `sudo docker ps`
4. Restart application: `sudo docker-compose restart`

---

**Drug Interaction Tracker** - Deployed successfully on VPS! 🚀 