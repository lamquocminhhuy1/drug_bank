# VPS Deployment Guide

This guide will help you deploy the Drug Interaction Tracker application on your VPS.

## Prerequisites

- Ubuntu 20.04+ or CentOS 8+
- Root or sudo access
- Domain name (optional but recommended)

## Step 1: Server Setup

### Update System
```bash
sudo apt update && sudo apt upgrade -y
```

### Install Docker
```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER

# Start Docker service
sudo systemctl start docker
sudo systemctl enable docker
```

### Install Docker Compose
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

## Step 2: Application Deployment

### Clone Repository
```bash
git clone <your-repository-url>
cd drug-management
```

### Configure Environment
Edit `docker-compose.yml` to update environment variables:

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8001:8001"
    environment:
      - DEBUG=False
      - SECRET_KEY=your-secure-secret-key-here
      - ALLOWED_HOSTS=your-domain.com,www.your-domain.com,localhost,127.0.0.1
    volumes:
      - ./media:/app/media
      - ./staticfiles:/app/staticfiles
    depends_on:
      - db
    restart: unless-stopped

  db:
    image: postgres:15
    environment:
      - POSTGRES_DB=drug_interaction
      - POSTGRES_USER=drug_user
      - POSTGRES_PASSWORD=your-secure-password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: unless-stopped

volumes:
  postgres_data:
```

### Deploy Application
```bash
# Build and start the application
docker-compose up -d --build

# Check if containers are running
docker-compose ps

# View logs
docker-compose logs -f
```

## Step 3: Nginx Configuration (Optional)

### Install Nginx
```bash
sudo apt install nginx -y
```

### Create Nginx Configuration
Create `/etc/nginx/sites-available/drug-interaction`:

```nginx
server {
    listen 80;
    server_name your-domain.com www.your-domain.com;

    location / {
        proxy_pass http://localhost:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /path/to/your/drug-management/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }

    location /media/ {
        alias /path/to/your/drug-management/media/;
        expires 30d;
        add_header Cache-Control "public, immutable";
    }
}
```

### Enable Site
```bash
sudo ln -s /etc/nginx/sites-available/drug-interaction /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

## Step 4: SSL Certificate (Optional)

### Install Certbot
```bash
sudo apt install certbot python3-certbot-nginx -y
```

### Obtain SSL Certificate
```bash
sudo certbot --nginx -d your-domain.com -d www.your-domain.com
```

## Step 5: Firewall Configuration

### Configure UFW
```bash
sudo ufw allow ssh
sudo ufw allow 80
sudo ufw allow 443
sudo ufw enable
```

## Step 6: Monitoring and Maintenance

### Create Systemd Service (Optional)
Create `/etc/systemd/system/drug-interaction.service`:

```ini
[Unit]
Description=Drug Interaction Tracker
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=yes
WorkingDirectory=/path/to/your/drug-management
ExecStart=/usr/local/bin/docker-compose up -d
ExecStop=/usr/local/bin/docker-compose down
TimeoutStartSec=0

[Install]
WantedBy=multi-user.target
```

### Enable Service
```bash
sudo systemctl enable drug-interaction.service
sudo systemctl start drug-interaction.service
```

## Step 7: Backup Strategy

### Create Backup Script
Create `backup.sh`:

```bash
#!/bin/bash
BACKUP_DIR="/backup/drug-interaction"
DATE=$(date +%Y%m%d_%H%M%S)

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup database
docker-compose exec -T db pg_dump -U drug_user drug_interaction > $BACKUP_DIR/db_backup_$DATE.sql

# Backup media files
tar -czf $BACKUP_DIR/media_backup_$DATE.tar.gz media/

# Keep only last 7 days of backups
find $BACKUP_DIR -name "*.sql" -mtime +7 -delete
find $BACKUP_DIR -name "*.tar.gz" -mtime +7 -delete

echo "Backup completed: $DATE"
```

### Setup Cron Job
```bash
# Add to crontab
crontab -e

# Add this line for daily backup at 2 AM
0 2 * * * /path/to/your/drug-management/backup.sh
```

## Troubleshooting

### Check Application Status
```bash
# Check container status
docker-compose ps

# View application logs
docker-compose logs web

# View database logs
docker-compose logs db
```

### Restart Application
```bash
docker-compose restart
```

### Update Application
```bash
# Pull latest changes
git pull

# Rebuild and restart
docker-compose up -d --build
```

### Database Issues
```bash
# Access database
docker-compose exec db psql -U drug_user -d drug_interaction

# Reset database (WARNING: This will delete all data)
docker-compose down
docker volume rm drug-management_postgres_data
docker-compose up -d
```

## Security Considerations

1. **Change default passwords** in docker-compose.yml
2. **Use strong SECRET_KEY** for Django
3. **Enable HTTPS** with SSL certificates
4. **Configure firewall** to only allow necessary ports
5. **Regular updates** of Docker images and system packages
6. **Monitor logs** for suspicious activity

## Performance Optimization

1. **Enable gzip compression** in Nginx
2. **Use CDN** for static files
3. **Configure caching** headers
4. **Monitor resource usage** with `docker stats`
5. **Scale horizontally** if needed with multiple containers

## Access URLs

- **Web Interface**: http://your-domain.com or http://your-server-ip:8001
- **API Documentation**: http://your-domain.com/api/ or http://your-server-ip:8001/api/
- **Admin Panel**: http://your-domain.com/admin/ or http://your-server-ip:8001/admin/

## Support

For issues and support:
1. Check the logs: `docker-compose logs`
2. Verify configuration files
3. Test connectivity: `curl http://localhost:8001/`
4. Check system resources: `docker stats` 