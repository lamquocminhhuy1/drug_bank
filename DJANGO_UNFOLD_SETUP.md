# Cài Đặt Django Unfold - Modern Admin Interface

## 🎯 Mục Tiêu

Thay thế giao diện admin mặc định của Django bằng Django Unfold để cung cấp:
- Giao diện admin hiện đại và đẹp mắt
- Better user experience
- Enhanced functionality
- Custom styling và branding

## 📦 Cài Đặt

### 1. **Thêm Dependencies**

#### `requirements.txt`:
```txt
django-unfold==0.20.0
```

#### Cài đặt:
```bash
pip install django-unfold==0.20.0
```

### 2. **Cập Nhật Settings**

#### `drug_interaction/settings.py`:
```python
INSTALLED_APPS = [
    'unfold',  # Django Unfold - Modern Admin Interface
    'django.contrib.admin',
    # ... other apps
]

# Django Unfold Configuration
UNFOLD = {
    "SITE_TITLE": "Drug Interaction Admin",
    "SITE_HEADER": "Drug Interaction Management",
    "SITE_SYMBOL": "💊",
    "SHOW_HISTORY": True,
    "SHOW_USER": True,
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [
            {
                "title": "Drug Management",
                "app": "drugs",
            },
        ],
    },
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255", 
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "196 181 253",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
}
```

### 3. **Cập Nhật Admin Configuration**

#### `drugs/admin.py`:
```python
from django.contrib import admin
from django.utils.html import format_html
from unfold.admin import ModelAdmin
from .models import Drug, DrugInteraction

@admin.register(Drug)
class DrugAdmin(ModelAdmin):
    list_display = ['id', 'ten_thuoc', 'phan_loai', 'nuoc_dk', 'sys_created_on', 'status_badge']
    list_filter = ['phan_loai', 'nuoc_dk', 'sys_created_on']
    search_fields = ['ten_thuoc', 'hoat_chat', 'id', 'nhom_thuoc']
    readonly_fields = ['sys_created_on', 'sys_updated_on', 'sys_id']
    ordering = ['ten_thuoc']
    
    # Unfold specific configurations
    list_per_page = 20
    list_max_show_all = 100
    
    fieldsets = (
        ('Thông tin cơ bản', {
            'fields': ('id', 'ten_thuoc', 'hoat_chat', 'phan_loai', 'nhom_thuoc', 'nuoc_dk')
        }),
        ('Thông tin bổ sung', {
            'fields': ('source_data', 'source_pdf', 'meta_data'),
            'classes': ('collapse',)
        }),
        ('Thông tin hệ thống', {
            'fields': ('sys_id', 'sys_created_by', 'sys_updated_by', 'sys_created_on', 'sys_updated_on', 'sys_mod_count', 'sys_tags'),
            'classes': ('collapse',)
        }),
    )
    
    def status_badge(self, obj):
        """Hiển thị badge cho trạng thái thuốc"""
        if obj.phan_loai == "Thuốc kê đơn":
            return format_html('<span class="badge bg-warning">Kê đơn</span>')
        else:
            return format_html('<span class="badge bg-success">Không kê đơn</span>')
    status_badge.short_description = 'Phân loại'

@admin.register(DrugInteraction)
class DrugInteractionAdmin(ModelAdmin):
    list_display = ['drug1', 'drug2', 'severity_badge', 'created_at', 'interaction_summary']
    list_filter = ['severity', 'created_at', 'updated_at']
    search_fields = ['drug1__ten_thuoc', 'drug2__ten_thuoc', 'mechanism', 'consequence', 'management']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    # Unfold specific configurations
    list_per_page = 15
    list_max_show_all = 100
    
    fieldsets = (
        ('Thuốc tương tác', {
            'fields': ('drug1', 'drug2')
        }),
        ('Thông tin tương tác', {
            'fields': ('severity', 'mechanism', 'consequence', 'management')
        }),
        ('Thông tin hệ thống', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def severity_badge(self, obj):
        """Hiển thị badge cho mức độ tương tác"""
        colors = {
            'contraindicated': 'danger',
            'major': 'warning', 
            'moderate': 'info',
            'minor': 'success'
        }
        color = colors.get(obj.severity, 'secondary')
        return format_html('<span class="badge bg-{}">{}</span>', color, obj.get_severity_display())
    severity_badge.short_description = 'Mức độ'
    
    def interaction_summary(self, obj):
        """Hiển thị tóm tắt tương tác"""
        return format_html(
            '<div class="text-muted small">{} → {}</div>',
            obj.drug1.ten_thuoc,
            obj.drug2.ten_thuoc
        )
    interaction_summary.short_description = 'Tương tác'
```

## 🚀 Truy Cập

### **Admin Interface:**
- **Admin Login**: http://localhost:8001/admin/
- **Username**: admin hoặc admin2
- **Password**: (được tạo khi tạo superuser)

## 🎨 Tính Năng Unfold

### 1. **Modern UI/UX**
- Clean và modern design
- Responsive layout
- Better typography
- Enhanced navigation

### 2. **Enhanced Functionality**
- **Badges**: Hiển thị trạng thái với màu sắc
- **Fieldsets**: Tổ chức form fields thành nhóm
- **Search**: Tìm kiếm nâng cao
- **Filters**: Bộ lọc cải tiến
- **Pagination**: Phân trang tối ưu

### 3. **Custom Branding**
- **Site Title**: "Drug Interaction Admin"
- **Site Header**: "Drug Interaction Management"
- **Site Symbol**: "💊" (pill emoji)
- **Custom Colors**: Purple theme

### 4. **Admin Features**
- **Status Badges**: Hiển thị phân loại thuốc
- **Severity Badges**: Hiển thị mức độ tương tác
- **Interaction Summary**: Tóm tắt tương tác
- **Collapsible Sections**: Thông tin hệ thống có thể ẩn/hiện

## 📋 Admin Models

### **Drug Model**
- **List Display**: ID, Tên thuốc, Phân loại, Nước đăng ký, Ngày tạo, Badge
- **Filters**: Phân loại, Nước đăng ký, Ngày tạo
- **Search**: Tên thuốc, Hoạt chất, ID, Nhóm thuốc
- **Fieldsets**: Thông tin cơ bản, bổ sung, hệ thống

### **DrugInteraction Model**
- **List Display**: Thuốc 1, Thuốc 2, Badge mức độ, Ngày tạo, Tóm tắt
- **Filters**: Mức độ, Ngày tạo, Ngày cập nhật
- **Search**: Tên thuốc, Cơ chế, Hậu quả, Quản lý
- **Fieldsets**: Thuốc tương tác, Thông tin tương tác, Hệ thống

## 🎨 Visual Enhancements

### **Badge System**
- **Drug Status**: 
  - 🟡 "Kê đơn" (Thuốc kê đơn)
  - 🟢 "Không kê đơn" (Thuốc không kê đơn)

- **Interaction Severity**:
  - 🔴 "Chống chỉ định" (contraindicated)
  - 🟡 "Tương tác nghiêm trọng" (major)
  - 🔵 "Tương tác trung bình" (moderate)
  - 🟢 "Tương tác nhẹ" (minor)

### **Layout Improvements**
- **Responsive Design**: Hoạt động tốt trên mobile
- **Better Spacing**: Khoảng cách hợp lý
- **Modern Typography**: Font chữ hiện đại
- **Color Scheme**: Purple theme chuyên nghiệp

## 🔧 Configuration Options

### **UNFOLD Settings**
```python
UNFOLD = {
    "SITE_TITLE": "Drug Interaction Admin",
    "SITE_HEADER": "Drug Interaction Management", 
    "SITE_SYMBOL": "💊",
    "SHOW_HISTORY": True,
    "SHOW_USER": True,
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": True,
        "navigation": [...]
    },
    "COLORS": {
        "primary": {...}
    }
}
```

### **ModelAdmin Features**
- **list_per_page**: Số items per page
- **list_max_show_all**: Tối đa items khi show all
- **fieldsets**: Tổ chức form fields
- **custom methods**: Badge và summary functions

## ✅ Kết Quả

### **Trước khi cài Unfold:**
- Giao diện admin mặc định của Django
- UI đơn giản, ít tính năng
- Không có visual enhancements

### **Sau khi cài Unfold:**
- ✅ Giao diện hiện đại và chuyên nghiệp
- ✅ Badge system cho trạng thái
- ✅ Enhanced search và filters
- ✅ Responsive design
- ✅ Custom branding
- ✅ Better user experience
- ✅ Collapsible sections
- ✅ Visual indicators

## 🎉 Kết Luận

Django Unfold đã được cài đặt thành công và cung cấp:
- **Modern Admin Interface**
- **Enhanced User Experience**
- **Visual Indicators**
- **Better Organization**
- **Custom Branding**

Truy cập http://localhost:8001/admin/ để xem giao diện admin mới! 🚀 