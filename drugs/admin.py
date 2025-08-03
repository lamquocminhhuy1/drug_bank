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