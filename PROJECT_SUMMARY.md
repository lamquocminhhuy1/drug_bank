# Drug Interaction Tracker - Tổng Quan Dự Án

## 🎯 Mục Tiêu Dự Án

Xây dựng một hệ thống web hoàn chỉnh để tra cứu tương tác thuốc với:
- **Web Interface**: Giao diện người dùng thân thiện
- **REST API**: API đầy đủ với documentation
- **Admin Panel**: Giao diện quản lý hiện đại
- **Dynamic Statistics**: Thống kê động từ database
- **Docker Support**: Triển khai dễ dàng

## 🏗️ Kiến Trúc Hệ Thống

### **Backend Stack**
- **Django 4.2.7**: Web framework chính
- **Django REST Framework**: API development
- **SQLite**: Database development
- **PostgreSQL**: Database production (Docker)

### **Frontend Stack**
- **Bootstrap 5**: UI framework
- **Font Awesome**: Icons
- **Django Templates**: Server-side rendering

### **Admin & Documentation**
- **Django Unfold**: Modern admin interface
- **Swagger/OpenAPI**: API documentation
- **drf-yasg**: Swagger integration

### **Deployment**
- **Docker**: Containerization
- **Docker Compose**: Multi-container setup
- **Gunicorn**: WSGI server
- **Whitenoise**: Static files serving

## 📁 Cấu Trúc Dự Án

```
drug-management/
├── drug_interaction/          # Django project
│   ├── settings.py           # Project settings
│   ├── urls.py              # Main URL configuration
│   └── wsgi.py              # WSGI configuration
├── drugs/                    # Main app
│   ├── models.py            # Database models
│   ├── views.py             # Views & API viewsets
│   ├── serializers.py       # API serializers
│   ├── admin.py             # Admin configuration
│   ├── urls.py              # Legacy URLs
│   ├── api_urls.py          # API URLs
│   ├── web_urls.py          # Web URLs
│   └── management/          # Custom commands
├── templates/                # HTML templates
│   ├── base.html            # Base template
│   └── drugs/               # App templates
├── static/                   # Static files
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker Compose
├── README.md                # Project documentation
└── DEPLOYMENT.md            # Deployment guide
```

## 🗄️ Database Models

### **Drug Model**
```python
class Drug(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    ten_thuoc = models.CharField(max_length=200)
    hoat_chat = models.TextField()
    phan_loai = models.CharField(max_length=100)
    nhom_thuoc = models.CharField(max_length=100)
    nuoc_dk = models.CharField(max_length=100)
    source_data = models.URLField()
    source_pdf = models.URLField()
    meta_data = models.CharField(max_length=200)
    # System fields...
```

### **DrugInteraction Model**
```python
class DrugInteraction(models.Model):
    drug1 = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name='interactions_as_drug1')
    drug2 = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name='interactions_as_drug2')
    mechanism = models.TextField()
    consequence = models.TextField()
    management = models.TextField()
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

## 🌐 Web Interface

### **Trang Chủ** (`/`)
- **Dynamic Statistics**: Thống kê động từ database
- **Search Functionality**: Tìm kiếm tương tác thuốc
- **Severity Breakdown**: Phân bố mức độ tương tác
- **Modern UI**: Bootstrap 5 + Font Awesome

### **Tìm Kiếm** (`/search/`)
- **Advanced Search**: Tìm theo tên thuốc, hoạt chất, cơ chế
- **Severity Filter**: Lọc theo mức độ tương tác
- **Results Display**: Hiển thị kết quả với pagination

### **Chi Tiết Thuốc** (`/drug/<id>/`)
- **Drug Information**: Thông tin chi tiết thuốc
- **Related Interactions**: Danh sách tương tác liên quan
- **Interactive Display**: Giao diện tương tác

### **Chi Tiết Tương Tác** (`/interaction/<id>/`)
- **Interaction Details**: Thông tin chi tiết tương tác
- **Severity Indicators**: Hiển thị mức độ với màu sắc
- **Management Guidelines**: Hướng dẫn quản lý

## 🔌 REST API

### **API Endpoints**
- **GET /api/**: API root với documentation links
- **GET /api/drugs/**: Danh sách thuốc với search
- **GET /api/drugs/{id}/**: Chi tiết thuốc
- **GET /api/interactions/**: Danh sách tương tác với filter
- **GET /api/interactions/{id}/**: Chi tiết tương tác
- **GET /api/interactions/search/**: Tìm kiếm tương tác
- **GET /api/stats/**: Thống kê tổng quan

### **API Documentation**
- **Swagger UI**: http://localhost:8001/api/swagger/
- **ReDoc**: http://localhost:8001/api/redoc/
- **JSON Schema**: http://localhost:8001/api/swagger.json
- **YAML Schema**: http://localhost:8001/api/swagger.yaml

### **API Features**
- **Pagination**: Phân trang tự động
- **Search & Filter**: Tìm kiếm và lọc nâng cao
- **Response Examples**: Ví dụ response
- **Parameter Validation**: Validation tham số
- **Error Handling**: Xử lý lỗi chi tiết

## 🛠️ Admin Interface

### **Django Unfold Integration**
- **Modern UI**: Giao diện hiện đại và responsive
- **Custom Branding**: Branding tùy chỉnh với emoji 💊
- **Enhanced Features**: Tính năng nâng cao

### **Drug Admin**
- **List Display**: ID, Tên thuốc, Phân loại, Badge
- **Status Badges**: Hiển thị phân loại thuốc
- **Fieldsets**: Tổ chức form fields
- **Search & Filter**: Tìm kiếm và lọc nâng cao

### **Interaction Admin**
- **Severity Badges**: Badge màu sắc cho mức độ
- **Interaction Summary**: Tóm tắt tương tác
- **Enhanced Display**: Hiển thị cải tiến
- **Collapsible Sections**: Phần có thể ẩn/hiện

## 📊 Dynamic Statistics

### **Real-time Data**
- **Total Drugs**: Số lượng thuốc trong database
- **Total Interactions**: Số lượng tương tác
- **Severity Breakdown**: Phân bố theo mức độ
- **Last Updated**: Thời gian cập nhật cuối

### **API Integration**
- **GET /api/stats/**: JSON endpoint cho thống kê
- **Auto-update**: Tự động cập nhật khi có dữ liệu mới
- **Caching**: Cache để tối ưu performance

## 🐳 Docker Support

### **Development**
```bash
# Local development
python manage.py runserver 8001
```

### **Production**
```bash
# Docker Compose
docker-compose up -d

# Docker build
docker build -t drug-interaction .
docker run -p 8001:8001 drug-interaction
```

### **Docker Configuration**
- **Multi-stage build**: Tối ưu image size
- **Non-root user**: Security best practices
- **Health checks**: Kiểm tra sức khỏe container
- **Volume mounts**: Persistent data

## 🚀 Deployment

### **Local Development**
```bash
# Setup
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Database
python manage.py makemigrations
python manage.py migrate

# Load data
python manage.py load_sample_data

# Run
python manage.py runserver 8001
```

### **VPS Deployment**
- **Nginx**: Reverse proxy
- **SSL/HTTPS**: Certbot integration
- **PostgreSQL**: Production database
- **Docker Compose**: Multi-container setup

## 📈 Tính Năng Nổi Bật

### **1. Modern Web Interface**
- ✅ Responsive design với Bootstrap 5
- ✅ Dynamic statistics từ database
- ✅ Advanced search functionality
- ✅ Interactive drug interaction display

### **2. Comprehensive API**
- ✅ RESTful API với Django REST Framework
- ✅ Swagger/OpenAPI documentation
- ✅ Interactive API testing
- ✅ Comprehensive error handling

### **3. Professional Admin**
- ✅ Django Unfold modern interface
- ✅ Custom branding và styling
- ✅ Enhanced data visualization
- ✅ Advanced filtering và search

### **4. Production Ready**
- ✅ Docker containerization
- ✅ Multi-environment support
- ✅ Security best practices
- ✅ Performance optimization

### **5. Developer Friendly**
- ✅ Comprehensive documentation
- ✅ Code organization
- ✅ Testing support
- ✅ Easy deployment

## 🎯 Truy Cập

### **Web Interface**
- **Homepage**: http://localhost:8001/
- **Search**: http://localhost:8001/search/
- **Drug Detail**: http://localhost:8001/drug/<id>/
- **Interaction Detail**: http://localhost:8001/interaction/<id>/

### **API Documentation**
- **Swagger UI**: http://localhost:8001/api/swagger/
- **ReDoc**: http://localhost:8001/api/redoc/
- **API Root**: http://localhost:8001/api/

### **Admin Panel**
- **Admin Login**: http://localhost:8001/admin/
- **Username**: admin hoặc admin2
- **Password**: (được tạo khi setup)

## 🎉 Kết Luận

Drug Interaction Tracker là một hệ thống hoàn chỉnh với:

- **🌐 Modern Web Interface**: Giao diện người dùng hiện đại
- **🔌 Comprehensive API**: API đầy đủ với documentation
- **🛠️ Professional Admin**: Panel quản lý chuyên nghiệp
- **📊 Dynamic Features**: Tính năng động và real-time
- **🐳 Production Ready**: Sẵn sàng triển khai production
- **📚 Well Documented**: Tài liệu đầy đủ và chi tiết

Hệ thống đã sẵn sàng để sử dụng và có thể mở rộng thêm các tính năng mới! 🚀 