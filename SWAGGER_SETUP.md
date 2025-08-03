# Cài Đặt Swagger/OpenAPI - Drug Interaction Tracker

## 🎯 Mục Tiêu

Thay thế trang default của Django REST Framework bằng Swagger/OpenAPI để cung cấp:
- Giao diện API documentation đẹp và chuyên nghiệp
- Interactive API testing
- Auto-generated documentation từ code
- Better developer experience

## 📦 Cài Đặt

### 1. **Thêm Dependencies**

#### `requirements.txt`:
```txt
drf-yasg==1.21.7
```

#### Cài đặt:
```bash
pip install drf-yasg==1.21.7
```

### 2. **Cập Nhật Settings**

#### `drug_interaction/settings.py`:
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'drf_yasg',  # Thêm dòng này
    'drugs',
]
```

### 3. **Cấu Hình API URLs**

#### `drugs/api_urls.py`:
```python
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

router = DefaultRouter()
router.register(r'drugs', views.DrugViewSet)
router.register(r'interactions', views.DrugInteractionViewSet)

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Drug Interaction API",
        default_version='v1',
        description="API để tra cứu tương tác thuốc",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@drug-interaction.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('stats/', views.api_stats, name='api_stats'),
    
    # Swagger URLs
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
```

### 4. **Cập Nhật Views với Documentation**

#### `drugs/views.py`:
```python
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class DrugViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint cho danh sách thuốc
    
    list:
        Trả về danh sách tất cả thuốc
    retrieve:
        Trả về thông tin chi tiết của một thuốc
    """
    # ... existing code ...

class DrugInteractionViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint cho danh sách tương tác thuốc
    
    list:
        Trả về danh sách tất cả tương tác thuốc
    retrieve:
        Trả về thông tin chi tiết của một tương tác
    search:
        Tìm kiếm tương tác theo từ khóa
    """
    
    @swagger_auto_schema(
        operation_description="Tìm kiếm tương tác thuốc theo từ khóa",
        manual_parameters=[
            openapi.Parameter(
                'q',
                openapi.IN_QUERY,
                description="Từ khóa tìm kiếm (tên thuốc, hoạt chất, cơ chế, hậu quả)",
                type=openapi.TYPE_STRING,
                required=False
            ),
            openapi.Parameter(
                'severity',
                openapi.IN_QUERY,
                description="Mức độ tương tác (contraindicated, major, moderate, minor)",
                type=openapi.TYPE_STRING,
                required=False,
                enum=['contraindicated', 'major', 'moderate', 'minor']
            )
        ],
        responses={
            200: DrugInteractionSerializer(many=True),
            400: "Bad Request"
        }
    )
    @action(detail=False, methods=['get'])
    def search(self, request):
        # ... existing code ...
```

## 🚀 Truy Cập

### **Swagger UI:**
- **Swagger UI**: http://localhost:8001/api/swagger/
- **ReDoc**: http://localhost:8001/api/redoc/
- **JSON Schema**: http://localhost:8001/api/swagger.json
- **YAML Schema**: http://localhost:8001/api/swagger.yaml

### **API Endpoints:**
- **API Root**: http://localhost:8001/api/
- **Drugs**: http://localhost:8001/api/drugs/
- **Interactions**: http://localhost:8001/api/interactions/
- **Stats**: http://localhost:8001/api/stats/

## 🎨 Tính Năng Swagger

### 1. **Interactive Documentation**
- Test API trực tiếp từ browser
- Auto-generated request/response examples
- Parameter validation
- Response schema visualization

### 2. **Auto-Generated Documentation**
- Tự động tạo từ docstrings
- Parameter descriptions
- Response schemas
- Error codes

### 3. **Multiple Formats**
- **Swagger UI**: Interactive interface
- **ReDoc**: Clean documentation
- **JSON/YAML**: Machine-readable schemas

### 4. **Features**
- ✅ Search functionality
- ✅ Filtering by severity
- ✅ Pagination
- ✅ Response examples
- ✅ Parameter validation
- ✅ Error handling

## 📋 API Endpoints Documentation

### **GET /api/drugs/**
- **Description**: Lấy danh sách tất cả thuốc
- **Parameters**: 
  - `q` (optional): Tìm kiếm theo tên thuốc, hoạt chất, nhóm thuốc
- **Response**: Paginated list of drugs

### **GET /api/drugs/{id}/**
- **Description**: Lấy thông tin chi tiết của một thuốc
- **Parameters**: `id` (required): ID của thuốc
- **Response**: Drug details

### **GET /api/interactions/**
- **Description**: Lấy danh sách tất cả tương tác thuốc
- **Parameters**:
  - `q` (optional): Tìm kiếm theo từ khóa
  - `severity` (optional): Lọc theo mức độ
- **Response**: Paginated list of interactions

### **GET /api/interactions/{id}/**
- **Description**: Lấy thông tin chi tiết của một tương tác
- **Parameters**: `id` (required): ID của tương tác
- **Response**: Interaction details

### **GET /api/interactions/search/**
- **Description**: Tìm kiếm tương tác thuốc
- **Parameters**:
  - `q` (optional): Từ khóa tìm kiếm
  - `severity` (optional): Mức độ tương tác
- **Response**: Filtered interactions

### **GET /api/stats/**
- **Description**: Lấy thống kê tổng quan
- **Response**: Application statistics

## 🔧 Troubleshooting

### **Lỗi thường gặp:**

1. **AssertionError với swagger_auto_schema**:
   - Chỉ sử dụng với `@action` hoặc `@api_view`
   - Không sử dụng với function views thông thường

2. **Import errors**:
   - Đảm bảo `drf-yasg` đã được cài đặt
   - Kiểm tra `INSTALLED_APPS`

3. **URL conflicts**:
   - Đảm bảo Swagger URLs không conflict với API routes

## ✅ Kết Quả

### **Trước khi cài Swagger:**
- Trang API default của Django REST Framework
- Giao diện đơn giản, ít tính năng
- Không có interactive testing

### **Sau khi cài Swagger:**
- ✅ Giao diện đẹp và chuyên nghiệp
- ✅ Interactive API testing
- ✅ Auto-generated documentation
- ✅ Parameter validation
- ✅ Response examples
- ✅ Multiple documentation formats
- ✅ Better developer experience

## 🎉 Kết Luận

Swagger/OpenAPI đã được cài đặt thành công và cung cấp:
- **Professional API documentation**
- **Interactive testing interface**
- **Auto-generated schemas**
- **Better developer experience**

Truy cập http://localhost:8001/api/swagger/ để xem giao diện mới! 🚀 