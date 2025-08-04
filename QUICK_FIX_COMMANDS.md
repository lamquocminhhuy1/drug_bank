# Quick Fix Commands for VPS Issues

## 🚨 **Immediate Fix Commands**

### **1. Stop and Fix Permissions**
```bash
# Stop containers
sudo docker-compose down

# Create directories with proper permissions
sudo mkdir -p static staticfiles media
sudo chmod 755 static staticfiles media
sudo chown -R 1000:1000 static staticfiles media

# Create database file with proper permissions
sudo touch db.sqlite3
sudo chmod 644 db.sqlite3
sudo chown 1000:1000 db.sqlite3

# Create static files structure
sudo mkdir -p static/css static/js static/images
sudo chmod -R 755 static
sudo chown -R 1000:1000 static
```

### **2. Rebuild and Start**
```bash
# Rebuild and start containers
sudo docker-compose up --build -d

# Check status
sudo docker-compose ps

# View logs
sudo docker-compose logs -f
```

### **3. Alternative: One-Command Fix**
```bash
# Download and run fix script
wget https://raw.githubusercontent.com/lamquocminhhuy1/drug_bank/main/fix_vps_issues.sh
sudo bash fix_vps_issues.sh
```

## 🔍 **Troubleshooting Commands**

### **Check Database File**
```bash
# Check if database file exists
ls -la db.sqlite3

# Check database permissions
sudo ls -la db.sqlite3

# Fix database permissions
sudo chmod 644 db.sqlite3
sudo chown 1000:1000 db.sqlite3
```

### **Check Static Files**
```bash
# Check static directory
ls -la static/

# Create static directory if missing
sudo mkdir -p static/css static/js static/images
sudo chmod -R 755 static
sudo chown -R 1000:1000 static
```

### **Check Container Logs**
```bash
# View all logs
sudo docker-compose logs

# View web container logs
sudo docker-compose logs web

# Follow logs in real-time
sudo docker-compose logs -f web
```

### **Reset Everything**
```bash
# Stop containers
sudo docker-compose down

# Remove containers and images
sudo docker-compose down --rmi all --volumes --remove-orphans

# Clean up Docker
sudo docker system prune -a -f

# Rebuild from scratch
sudo docker-compose up --build -d
```

## 🎯 **Specific Error Fixes**

### **"unable to open database file"**
```bash
# Fix database permissions
sudo touch db.sqlite3
sudo chmod 644 db.sqlite3
sudo chown 1000:1000 db.sqlite3

# Restart containers
sudo docker-compose restart
```

### **"staticfiles.W004" Warning**
```bash
# Create static directory
sudo mkdir -p static/css static/js static/images
sudo chmod -R 755 static
sudo chown -R 1000:1000 static

# Restart containers
sudo docker-compose restart
```

### **Permission Denied Errors**
```bash
# Fix all permissions
sudo chown -R 1000:1000 .
sudo chmod -R 755 static staticfiles media
sudo chmod 644 db.sqlite3

# Restart containers
sudo docker-compose restart
```

## ✅ **Verification Commands**

### **Check Application Status**
```bash
# Test web interface
curl -I http://localhost:8001/

# Test API
curl -I http://localhost:8001/api/

# Check container status
sudo docker-compose ps
```

### **Check File Permissions**
```bash
# Check database file
ls -la db.sqlite3

# Check static directory
ls -la static/

# Check all files
ls -la
```

## 🚀 **Complete Reset (Nuclear Option)**

If nothing works, use this complete reset:

```bash
# Stop everything
sudo docker-compose down

# Remove everything
sudo docker system prune -a -f
sudo rm -rf static staticfiles media db.sqlite3

# Recreate directories
sudo mkdir -p static/css static/js static/images staticfiles media
sudo chmod -R 755 static staticfiles media
sudo chown -R 1000:1000 static staticfiles media

# Create database file
sudo touch db.sqlite3
sudo chmod 644 db.sqlite3
sudo chown 1000:1000 db.sqlite3

# Rebuild everything
sudo docker-compose up --build -d
```

## 📞 **If Still Having Issues**

1. **Check Docker logs**: `sudo docker-compose logs -f`
2. **Check system resources**: `free -h && df -h`
3. **Check Docker status**: `sudo systemctl status docker`
4. **Restart Docker**: `sudo systemctl restart docker`
5. **Check firewall**: `sudo ufw status`

---

**These commands should fix the database and static files issues!** 🔧 