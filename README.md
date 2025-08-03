# Drug Interaction Tracker

A Django web application for tracking and searching drug-drug interactions based on data from the Vietnamese Ministry of Health. This application provides both a web interface and REST API for accessing drug interaction information.

## Features

- 🔍 **Smart Search**: Search by drug names, active ingredients, mechanisms, or consequences
- 📊 **Severity Classification**: Interactions categorized by severity levels (Contraindicated, Major, Moderate, Minor)
- 📱 **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- 🔌 **REST API**: Full API support for integration with other systems
- 🎨 **Modern UI**: Beautiful and intuitive user interface with Bootstrap 5

## Technology Stack

- **Backend**: Django 4.2.7
- **API**: Django REST Framework 3.14.0
- **Frontend**: Bootstrap 5, Font Awesome
- **Database**: SQLite (development) / PostgreSQL (production)
- **Deployment**: Docker, Gunicorn

## Quick Start

### Prerequisites

- Python 3.11+
- pip
- Docker (for containerized deployment)

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd drug-management
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser (optional)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver 8001
   ```

7. **Access the application**
   - Web Interface: http://localhost:8001
   - Admin Panel: http://localhost:8001/admin
   - API Documentation: http://localhost:8001/api/

### Docker Deployment

1. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

2. **Access the application**
   - Web Interface: http://localhost:8001
   - API: http://localhost:8001/api/

### Manual Docker Build

1. **Build the Docker image**
   ```bash
   docker build -t drug-interaction-tracker .
   ```

2. **Run the container**
   ```bash
   docker run -p 8001:8001 drug-interaction-tracker
   ```

## API Endpoints

### Drugs
- `GET /api/drugs/` - List all drugs
- `GET /api/drugs/?q=<search_term>` - Search drugs
- `GET /api/drugs/<id>/` - Get specific drug details

### Interactions
- `GET /api/interactions/` - List all interactions
- `GET /api/interactions/?q=<search_term>` - Search interactions
- `GET /api/interactions/?severity=<severity>` - Filter by severity
- `GET /api/interactions/<id>/` - Get specific interaction details
- `GET /api/interactions/search/?query=<query>&severity=<severity>` - Advanced search

### Example API Usage

```bash
# Search for interactions containing "itraconazol"
curl "http://localhost:8001/api/interactions/?q=itraconazol"

# Get interactions with major severity
curl "http://localhost:8001/api/interactions/?severity=major"

# Search drugs by name
curl "http://localhost:8001/api/drugs/?q=Corinell"
```

## Data Model

### Drug Model
```python
{
    "id": "VN-16282-13",
    "ten_thuoc": "Corinell",
    "hoat_chat": "L-Cystine; Choline Hydrogen Tartrate",
    "phan_loai": "Thuốc không kê đơn",
    "nhom_thuoc": "",
    "nuoc_dk": "Hàn Quốc",
    "source_data": "https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Corinell&id=VN-16282-13",
    "source_pdf": "https://cdn.drugbank.vn/1555036581572_1881_80Nhãn 80.pdf",
    # ... other fields
}
```

### Drug Interaction Model
```python
{
    "drug1": "Drug object",
    "drug2": "Drug object", 
    "mechanism": "Cơ chế tương tác",
    "consequence": "Hậu quả",
    "management": "Xử trí",
    "severity": "contraindicated|major|moderate|minor"
}
```

## Search Features

### Web Interface
- **Basic Search**: Enter drug names or active ingredients
- **Advanced Filtering**: Filter by interaction severity
- **Real-time Results**: Instant search results with pagination

### API Search
- **Text Search**: Search in drug names, active ingredients, mechanisms, consequences
- **Severity Filtering**: Filter by interaction severity level
- **Combined Queries**: Use multiple parameters for precise searches

## Deployment

### Production Settings

1. **Environment Variables**
   ```bash
   DEBUG=False
   SECRET_KEY=your-secure-secret-key
   ALLOWED_HOSTS=your-domain.com,www.your-domain.com
   ```

2. **Database Configuration**
   - Use PostgreSQL for production
   - Configure database connection in settings.py

3. **Static Files**
   ```bash
   python manage.py collectstatic
   ```

4. **Security**
   - Use HTTPS in production
   - Configure CORS settings
   - Set up proper firewall rules

### VPS Deployment

1. **Install Docker and Docker Compose**
   ```bash
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Docker
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   
   # Install Docker Compose
   sudo curl -L "https://github.com/docker/compose/releases/download/v2.20.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
   sudo chmod +x /usr/local/bin/docker-compose
   ```

2. **Deploy the application**
   ```bash
   # Clone repository
   git clone <repository-url>
   cd drug-management
   
   # Update environment variables in docker-compose.yml
   # Build and run
   docker-compose up -d --build
   ```

3. **Configure Nginx (optional)**
   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://localhost:8001;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
       }
   }
   ```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data source: Vietnamese Ministry of Health
- Reference: [Medica.wiki](https://medica.wiki/tra-cuu-tuong-tac-thuoc/)
- Icons: Font Awesome
- UI Framework: Bootstrap 5

## Support

For support and questions, please open an issue in the repository or contact the development team. 