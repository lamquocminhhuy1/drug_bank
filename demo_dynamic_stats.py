#!/usr/bin/env python3
"""
Demo script để thêm dữ liệu và xem thống kê thay đổi
"""

import os
import sys
import django
import requests
import time

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drug_interaction.settings')
django.setup()

from drugs.models import Drug, DrugInteraction

def get_stats():
    """Lấy thống kê từ API"""
    try:
        response = requests.get('http://localhost:8001/api/stats/')
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return None

def add_sample_drug():
    """Thêm một thuốc mẫu"""
    drug_data = {
        'id': f'VN-{int(time.time())}',
        'ten_thuoc': f'Thuốc Demo {int(time.time())}',
        'hoat_chat': 'Demo Active Ingredient',
        'phan_loai': 'Thuốc kê đơn',
        'nhom_thuoc': 'Thuốc demo',
        'nuoc_dk': 'Việt Nam',
        'source_data': 'https://demo.example.com',
        'source_pdf': '',
        'meta_data': '',
        'sys_id': f'demo_{int(time.time())}',
        'sys_created_by': 'demo',
        'sys_updated_by': 'demo',
        'sys_mod_count': '1',
        'sys_tags': '',
    }
    
    drug = Drug.objects.create(**drug_data)
    print(f"✅ Đã thêm thuốc: {drug.ten_thuoc}")
    return drug

def add_sample_interaction(drug1, drug2):
    """Thêm một tương tác mẫu"""
    interaction_data = {
        'drug1': drug1,
        'drug2': drug2,
        'mechanism': 'Demo mechanism',
        'consequence': 'Demo consequence',
        'management': 'Demo management',
        'severity': 'moderate',
    }
    
    interaction = DrugInteraction.objects.create(**interaction_data)
    print(f"✅ Đã thêm tương tác: {drug1.ten_thuoc} - {drug2.ten_thuoc}")
    return interaction

def main():
    print("🎯 Demo Thống Kê Động - Drug Interaction Tracker")
    print("=" * 50)
    
    # Hiển thị thống kê ban đầu
    print("\n📊 Thống kê ban đầu:")
    stats = get_stats()
    if stats:
        print(f"   • Tổng số thuốc: {stats['total_drugs']}")
        print(f"   • Tổng số tương tác: {stats['total_interactions']}")
        print("   • Phân bố mức độ:")
        for breakdown in stats['severity_breakdown']:
            print(f"     - {breakdown['label']}: {breakdown['count']}")
    
    # Thêm thuốc mới
    print("\n➕ Thêm thuốc mới...")
    new_drug = add_sample_drug()
    
    # Hiển thị thống kê sau khi thêm thuốc
    print("\n📊 Thống kê sau khi thêm thuốc:")
    stats = get_stats()
    if stats:
        print(f"   • Tổng số thuốc: {stats['total_drugs']}")
        print(f"   • Tổng số tương tác: {stats['total_interactions']}")
    
    # Thêm tương tác mới
    print("\n➕ Thêm tương tác mới...")
    existing_drug = Drug.objects.first()
    if existing_drug and new_drug.id != existing_drug.id:
        new_interaction = add_sample_interaction(new_drug, existing_drug)
        
        # Hiển thị thống kê sau khi thêm tương tác
        print("\n📊 Thống kê sau khi thêm tương tác:")
        stats = get_stats()
        if stats:
            print(f"   • Tổng số thuốc: {stats['total_drugs']}")
            print(f"   • Tổng số tương tác: {stats['total_interactions']}")
            print("   • Phân bố mức độ:")
            for breakdown in stats['severity_breakdown']:
                print(f"     - {breakdown['label']}: {breakdown['count']}")
    
    print("\n🌐 Truy cập web interface: http://localhost:8001")
    print("🔌 API Stats: http://localhost:8001/api/stats/")
    print("\n✅ Demo hoàn thành!")

if __name__ == '__main__':
    main() 