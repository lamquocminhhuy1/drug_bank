# Drug Interaction Tracker

A comprehensive Django web application for tracking drug-drug interactions with modern UI, REST API, and professional admin interface.

## 🚀 **Quick Start (One Command)**

### Prerequisites
- Docker
- Docker Compose

### Run Application
```bash
# Clone repository
git clone https://github.com/lamquocminhhuy1/drug_bank.git
cd drug_bank

# Run application (everything will be set up automatically)
./run.sh
```

### Access Application
- **Web Interface**: http://localhost:8001/
- **API Documentation**: http://localhost:8001/api/swagger/
- **Admin Panel**: http://localhost:8001/admin/
- **API Root**: http://localhost:8001/api/

### Admin Credentials
- **Username**: admin
- **Password**: admin123456

## 🛠️ **Manual Setup**

### Step 1: Clone Repository
```bash
git clone https://github.com/lamquocminhhuy1/drug_bank.git
cd drug_bank
```

### Step 2: Create Directories
```bash
mkdir -p static staticfiles media
```

### Step 3: Set Permissions
```bash
chmod 755 static staticfiles media
touch db.sqlite3
chmod 644 db.sqlite3
```

### Step 4: Run Application
```bash
docker-compose up --build -d
```

## 🎯 Features

### 🌐 Web Interface
- **Modern UI**: Bootstrap 5 responsive design
- **Dynamic Statistics**: Real-time data from database
- **Advanced Search**: Search by drug name, active ingredient, mechanism
- **Interactive Display**: Beautiful drug interaction visualization

### 🔌 REST API
- **Comprehensive Endpoints**: Full CRUD operations
- **Swagger Documentation**: Interactive API testing
- **Search & Filter**: Advanced query capabilities
- **Pagination**: Optimized data loading

### 🛠️ Admin Interface
- **Django Unfold**: Modern admin interface
- **Custom Branding**: Professional styling with emoji 💊
- **Enhanced Visualization**: Status badges and severity indicators
- **Advanced Features**: Search, filter, and data management

### 📊 Dynamic Features
- **Real-time Statistics**: Auto-updating from database
- **Severity Breakdown**: Visual distribution of interaction levels
- **Sample Data**: Pre-loaded with 9 drugs and 9 interactions

## 🐳 Docker Support

### Production Ready
- **Single container setup**: Web app with SQLite database
- **Environment variables**: Configurable settings
- **Health checks**: Application monitoring
- **Volume persistence**: Data persistence across restarts

### Docker Commands
```bash
# Start the application
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the application
docker-compose down

# Rebuild and restart
docker-compose up --build -d
```

## 📋 API Endpoints

### Core Endpoints
- `GET /api/` - API root with documentation links
- `GET /api/drugs/` - List all drugs with search
- `GET /api/drugs/{id}/` - Get drug details
- `GET /api/interactions/` - List all interactions with filter
- `GET /api/interactions/{id}/` - Get interaction details
- `GET /api/interactions/search/` - Search interactions
- `GET /api/stats/` - Get application statistics

### Documentation
- **Swagger UI**: http://localhost:8001/api/swagger/
- **ReDoc**: http://localhost:8001/api/redoc/
- **JSON Schema**: http://localhost:8001/api/swagger.json

## 🗄️ Database Models

### Drug Model
- Drug information (name, active ingredient, classification)
- Source data and metadata
- System tracking fields

### DrugInteraction Model
- Drug pairs and interaction details
- Mechanism, consequence, and management
- Severity levels (contraindicated, major, moderate, minor)
- Timestamps and tracking

## 🎨 Admin Features

### Drug Management
- **Status Badges**: Visual drug classification indicators
- **Fieldsets**: Organized form sections
- **Advanced Search**: Multi-field search capabilities
- **Bulk Operations**: Efficient data management

### Interaction Management
- **Severity Badges**: Color-coded interaction levels
- **Interaction Summary**: Quick overview of drug pairs
- **Enhanced Display**: Improved data visualization
- **Collapsible Sections**: Organized information display

## 🚀 Deployment

### VPS Deployment
See [VPS_DEPLOYMENT.md](VPS_DEPLOYMENT.md) for detailed VPS deployment instructions.

### Environment Variables
```bash
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=your-domain.com
```

## 📊 Sample Data

The application comes pre-loaded with:
- **9 Drugs**: Various classifications and countries
- **9 Interactions**: Different severity levels
- **Admin User**: Ready-to-use admin account

### Sample Drugs
- Itraconazol (Antifungal)
- Dabigatran (Anticoagulant)
- Aceclofenac (NSAID)
- Ketorolac (NSAID)
- Tramadol (Opioid)
- Corinell (Supplement)
- Warfarin (Anticoagulant)
- Aspirin (NSAID)

## 🔧 Troubleshooting

### Common Issues
1. **Port already in use**: Change port in docker-compose.yml
2. **Database file**: Check if db.sqlite3 exists and has proper permissions
3. **Static files**: Run `python manage.py collectstatic`

### Logs
```bash
# View application logs
docker-compose logs -f web
```

### Database Management
```bash
# Backup database
cp db.sqlite3 backup.sqlite3

# Restore database
cp backup.sqlite3 db.sqlite3

# Reset database (will lose all data)
rm db.sqlite3
docker-compose up --build -d
```

## 📚 Documentation

- [Project Summary](PROJECT_SUMMARY.md) - Complete project overview
- [Swagger Setup](SWAGGER_SETUP.md) - API documentation setup
- [Django Unfold Setup](DJANGO_UNFOLD_SETUP.md) - Admin interface setup
- [VPS Deployment Guide](VPS_DEPLOYMENT.md) - VPS deployment instructions
- [Quick Fix Commands](QUICK_FIX_COMMANDS.md) - Troubleshooting commands

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🎉 Acknowledgments

- Django community for the excellent framework
- Bootstrap for the responsive UI components
- Font Awesome for the beautiful icons
- Django Unfold for the modern admin interface
- Swagger/OpenAPI for the API documentation

---

**Drug Interaction Tracker** - Modern, comprehensive drug interaction management system! 💊 