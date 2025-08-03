from django.db import models
from django.utils import timezone


class Drug(models.Model):
    """Model for storing drug information"""
    id = models.CharField(max_length=50, primary_key=True)
    ten_thuoc = models.CharField(max_length=255, verbose_name="Tên thuốc")
    hoat_chat = models.TextField(verbose_name="Hoạt chất", blank=True)
    phan_loai = models.CharField(max_length=100, verbose_name="Phân loại", blank=True)
    nhom_thuoc = models.CharField(max_length=100, verbose_name="Nhóm thuốc", blank=True)
    nuoc_dk = models.CharField(max_length=100, verbose_name="Nước đăng ký", blank=True)
    source_data = models.URLField(verbose_name="Nguồn dữ liệu", blank=True)
    source_pdf = models.URLField(verbose_name="Nguồn PDF", blank=True)
    meta_data = models.CharField(max_length=255, verbose_name="Meta data", blank=True)
    sys_id = models.CharField(max_length=50, verbose_name="System ID", blank=True)
    sys_created_by = models.CharField(max_length=100, verbose_name="Tạo bởi", blank=True)
    sys_updated_by = models.CharField(max_length=100, verbose_name="Cập nhật bởi", blank=True)
    sys_created_on = models.DateTimeField(verbose_name="Ngày tạo", default=timezone.now)
    sys_updated_on = models.DateTimeField(verbose_name="Ngày cập nhật", default=timezone.now)
    sys_mod_count = models.CharField(max_length=10, verbose_name="Số lần sửa đổi", blank=True)
    sys_tags = models.TextField(verbose_name="Tags", blank=True)

    class Meta:
        verbose_name = "Thuốc"
        verbose_name_plural = "Thuốc"
        ordering = ['ten_thuoc']

    def __str__(self):
        return self.ten_thuoc


class DrugInteraction(models.Model):
    """Model for storing drug-drug interactions"""
    SEVERITY_CHOICES = [
        ('contraindicated', 'Chống chỉ định'),
        ('major', 'Tương tác nghiêm trọng'),
        ('moderate', 'Tương tác trung bình'),
        ('minor', 'Tương tác nhẹ'),
    ]

    drug1 = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name='interactions_as_drug1', verbose_name="Thuốc 1")
    drug2 = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name='interactions_as_drug2', verbose_name="Thuốc 2")
    mechanism = models.TextField(verbose_name="Cơ chế tương tác")
    consequence = models.TextField(verbose_name="Hậu quả")
    management = models.TextField(verbose_name="Xử trí")
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='moderate', verbose_name="Mức độ")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Ngày tạo")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Ngày cập nhật")

    class Meta:
        verbose_name = "Tương tác thuốc"
        verbose_name_plural = "Tương tác thuốc"
        unique_together = ['drug1', 'drug2']
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.drug1.ten_thuoc} - {self.drug2.ten_thuoc}"

    def get_severity_color(self):
        """Return Bootstrap color class based on severity"""
        colors = {
            'contraindicated': 'danger',
            'major': 'warning',
            'moderate': 'info',
            'minor': 'success',
        }
        return colors.get(self.severity, 'secondary') 