from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import transaction
from drugs.models import Drug, DrugInteraction
import os


class Command(BaseCommand):
    help = 'Load sample drug and interaction data'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')
        
        # Create superuser if it doesn't exist
        if not User.objects.filter(username='admin').exists():
            self.stdout.write('Creating admin superuser...')
            admin_user = User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123456'
            )
            self.stdout.write(
                self.style.SUCCESS(f'Superuser created: admin/admin123456')
            )
        else:
            self.stdout.write('Admin user already exists')

        # Sample drug data
        drugs_data = [
            {
                'id': 'VN-001-001',
                'ten_thuoc': 'Itraconazol',
                'hoat_chat': 'Itraconazole',
                'phan_loai': 'Thuốc kê đơn',
                'nhom_thuoc': 'Thuốc kháng nấm',
                'nuoc_dk': 'Việt Nam',
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Itraconazol&id=VN-001-001',
                'source_pdf': 'https://cdn.drugbank.vn/1555036581572_1881_80Nhãn 80.pdf',
                'meta_data': '1555036581572_1881_80Nhãn 80.pdf',
                'sys_id': '00124b5dc37b121065eb3fac05013175',
                'sys_created_by': 'lamquocminhhuy',
                'sys_updated_by': 'lamquocminhhuy',
                'sys_created_on': '2025-02-17 21:54:33',
                'sys_updated_on': '2025-02-17 21:54:33',
                'sys_mod_count': '1',
                'sys_tags': '',
            },
            {
                'id': 'VN-002-001',
                'ten_thuoc': 'Dabigatran',
                'hoat_chat': 'Dabigatran etexilate',
                'phan_loai': 'Thuốc kê đơn',
                'nhom_thuoc': 'Thuốc chống đông máu',
                'nuoc_dk': 'Việt Nam',
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Dabigatran&id=VN-002-001',
                'source_pdf': 'https://cdn.drugbank.vn/1555036581572_1881_80Nhãn 80.pdf',
                'meta_data': '1555036581572_1881_80Nhãn 80.pdf',
                'sys_id': '00124b5dc37b121065eb3fac05013176',
                'sys_created_by': 'lamquocminhhuy',
                'sys_updated_by': 'lamquocminhhuy',
                'sys_created_on': '2025-02-17 21:54:33',
                'sys_updated_on': '2025-02-17 21:54:33',
                'sys_mod_count': '1',
                'sys_tags': '',
            },
            {
                'id': 'VN-003-001',
                'ten_thuoc': 'Aceclofenac',
                'hoat_chat': 'Aceclofenac',
                'phan_loai': 'Thuốc kê đơn',
                'nhom_thuoc': 'Thuốc chống viêm không steroid',
                'nuoc_dk': 'Việt Nam',
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Aceclofenac&id=VN-003-001',
                'source_pdf': 'https://cdn.drugbank.vn/1555036581572_1881_80Nhãn 80.pdf',
                'meta_data': '1555036581572_1881_80Nhãn 80.pdf',
                'sys_id': '00124b5dc37b121065eb3fac05013177',
                'sys_created_by': 'lamquocminhhuy',
                'sys_updated_by': 'lamquocminhhuy',
                'sys_created_on': '2025-02-17 21:54:33',
                'sys_updated_on': '2025-02-17 21:54:33',
                'sys_mod_count': '1',
                'sys_tags': '',
            },
            {
                'id': 'VN-004-001',
                'ten_thuoc': 'Ketorolac',
                'hoat_chat': 'Ketorolac tromethamine',
                'phan_loai': 'Thuốc kê đơn',
                'nhom_thuoc': 'Thuốc chống viêm không steroid',
                'nuoc_dk': 'Việt Nam',
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Ketorolac&id=VN-004-001',
                'source_pdf': 'https://cdn.drugbank.vn/1555036581572_1881_80Nhãn 80.pdf',
                'meta_data': '1555036581572_1881_80Nhãn 80.pdf',
                'sys_id': '00124b5dc37b121065eb3fac05013178',
                'sys_created_by': 'lamquocminhhuy',
                'sys_updated_by': 'lamquocminhhuy',
                'sys_created_on': '2025-02-17 21:54:33',
                'sys_updated_on': '2025-02-17 21:54:33',
                'sys_mod_count': '1',
                'sys_tags': '',
            },
            {
                'id': 'VN-005-001',
                'ten_thuoc': 'Tramadol',
                'hoat_chat': 'Tramadol hydrochloride',
                'phan_loai': 'Thuốc kê đơn',
                'nhom_thuoc': 'Thuốc giảm đau opioid',
                'nuoc_dk': 'Việt Nam',
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Tramadol&id=VN-005-001',
                'source_pdf': 'https://cdn.drugbank.vn/1555036581572_1881_80Nhãn 80.pdf',
                'meta_data': '1555036581572_1881_80Nhãn 80.pdf',
                'sys_id': '00124b5dc37b121065eb3fac05013179',
                'sys_created_by': 'lamquocminhhuy',
                'sys_updated_by': 'lamquocminhhuy',
                'sys_created_on': '2025-02-17 21:54:33',
                'sys_updated_on': '2025-02-17 21:54:33',
                'sys_mod_count': '1',
                'sys_tags': '',
            },
            {
                'id': 'VN-16282-13',
                'ten_thuoc': 'Corinell',
                'hoat_chat': 'L-Cystine; Choline Hydrogen Tartrate',
                'phan_loai': 'Thuốc không kê đơn',
                'nhom_thuoc': 'Thực phẩm chức năng',
                'nuoc_dk': 'Hàn Quốc',
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Corinell&id=VN-16282-13',
                'source_pdf': 'https://cdn.drugbank.vn/1555036581572_1881_80Nhãn 80.pdf',
                'meta_data': '1555036581572_1881_80Nhãn 80.pdf',
                'sys_id': '00124b5dc37b121065eb3fac05013180',
                'sys_created_by': 'lamquocminhhuy',
                'sys_updated_by': 'lamquocminhhuy',
                'sys_created_on': '2025-02-17 21:54:33',
                'sys_updated_on': '2025-02-17 21:54:33',
                'sys_mod_count': '1',
                'sys_tags': '',
            },
            {
                'id': 'VN-006-001',
                'ten_thuoc': 'Warfarin',
                'hoat_chat': 'Warfarin sodium',
                'phan_loai': 'Thuốc kê đơn',
                'nhom_thuoc': 'Thuốc chống đông máu',
                'nuoc_dk': 'Việt Nam',
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Warfarin&id=VN-006-001',
                'source_pdf': 'https://cdn.drugbank.vn/1555036581572_1881_80Nhãn 80.pdf',
                'meta_data': '1555036581572_1881_80Nhãn 80.pdf',
                'sys_id': '00124b5dc37b121065eb3fac05013181',
                'sys_created_by': 'lamquocminhhuy',
                'sys_updated_by': 'lamquocminhhuy',
                'sys_created_on': '2025-02-17 21:54:33',
                'sys_updated_on': '2025-02-17 21:54:33',
                'sys_mod_count': '1',
                'sys_tags': '',
            },
            {
                'id': 'VN-007-001',
                'ten_thuoc': 'Aspirin',
                'hoat_chat': 'Acetylsalicylic acid',
                'phan_loai': 'Thuốc không kê đơn',
                'nhom_thuoc': 'Thuốc chống viêm không steroid',
                'nuoc_dk': 'Việt Nam',
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Aspirin&id=VN-007-001',
                'source_pdf': 'https://cdn.drugbank.vn/1555036581572_1881_80Nhãn 80.pdf',
                'meta_data': '1555036581572_1881_80Nhãn 80.pdf',
                'sys_id': '00124b5dc37b121065eb3fac05013182',
                'sys_created_by': 'lamquocminhhuy',
                'sys_updated_by': 'lamquocminhhuy',
                'sys_created_on': '2025-02-17 21:54:33',
                'sys_updated_on': '2025-02-17 21:54:33',
                'sys_mod_count': '1',
                'sys_tags': '',
            },
        ]

        # Sample interaction data
        interactions_data = [
            {
                'drug1_id': 'VN-001-001',  # Itraconazol
                'drug2_id': 'VN-002-001',  # Dabigatran
                'mechanism': 'Itraconazol ức chế CYP3A4 làm giảm chuyển hóa của dabigatran',
                'consequence': 'Tăng nồng độ dabigatran, tăng nguy cơ xuất huyết',
                'management': 'Tránh sử dụng đồng thời. Theo dõi chặt chẽ nếu cần thiết.',
                'severity': 'contraindicated',
            },
            {
                'drug1_id': 'VN-003-001',  # Aceclofenac
                'drug2_id': 'VN-004-001',  # Ketorolac
                'mechanism': 'Cả hai đều là NSAID, tăng nguy cơ tác dụng phụ',
                'consequence': 'Tăng nguy cơ loét dạ dày, xuất huyết tiêu hóa',
                'management': 'Tránh sử dụng đồng thời. Chọn một trong hai thuốc.',
                'severity': 'contraindicated',
            },
            {
                'drug1_id': 'VN-005-001',  # Tramadol
                'drug2_id': 'VN-004-001',  # Ketorolac
                'mechanism': 'Tương tác dược động học nhẹ',
                'consequence': 'Có thể tăng tác dụng giảm đau',
                'management': 'Theo dõi bệnh nhân khi sử dụng đồng thời.',
                'severity': 'moderate',
            },
            {
                'drug1_id': 'VN-001-001',  # Itraconazol
                'drug2_id': 'VN-005-001',  # Tramadol
                'mechanism': 'Itraconazol ức chế CYP2D6 làm tăng nồng độ tramadol',
                'consequence': 'Tăng tác dụng và độc tính của tramadol',
                'management': 'Giảm liều tramadol và theo dõi chặt chẽ.',
                'severity': 'major',
            },
            {
                'drug1_id': 'VN-002-001',  # Dabigatran
                'drug2_id': 'VN-004-001',  # Ketorolac
                'mechanism': 'NSAID làm tăng nguy cơ xuất huyết với thuốc chống đông',
                'consequence': 'Tăng nguy cơ xuất huyết nghiêm trọng',
                'management': 'Tránh sử dụng đồng thời. Theo dõi INR nếu cần.',
                'severity': 'major',
            },
            {
                'drug1_id': 'VN-006-001',  # Warfarin
                'drug2_id': 'VN-007-001',  # Aspirin
                'mechanism': 'Hiệp đồng tác dụng chống đông máu',
                'consequence': 'Tăng nguy cơ xuất huyết nghiêm trọng',
                'management': 'Tránh sử dụng đồng thời. Theo dõi INR chặt chẽ nếu cần thiết.',
                'severity': 'major',
            },
            {
                'drug1_id': 'VN-006-001',  # Warfarin
                'drug2_id': 'VN-001-001',  # Itraconazol
                'mechanism': 'Itraconazol ức chế CYP2C9 làm giảm chuyển hóa của warfarin',
                'consequence': 'Tăng nồng độ warfarin, tăng nguy cơ xuất huyết',
                'management': 'Theo dõi INR chặt chẽ và điều chỉnh liều warfarin.',
                'severity': 'major',
            },
            {
                'drug1_id': 'VN-007-001',  # Aspirin
                'drug2_id': 'VN-005-001',  # Tramadol
                'mechanism': 'Tương tác dược động học nhẹ',
                'consequence': 'Có thể tăng tác dụng giảm đau',
                'management': 'Theo dõi bệnh nhân khi sử dụng đồng thời.',
                'severity': 'minor',
            },
            {
                'drug1_id': 'VN-003-001',  # Aceclofenac
                'drug2_id': 'VN-007-001',  # Aspirin
                'mechanism': 'Cả hai đều là NSAID',
                'consequence': 'Tăng nguy cơ tác dụng phụ trên đường tiêu hóa',
                'management': 'Tránh sử dụng đồng thời. Chọn một trong hai thuốc.',
                'severity': 'moderate',
            },
        ]

        with transaction.atomic():
            # Create drugs
            for drug_data in drugs_data:
                drug, created = Drug.objects.get_or_create(
                    id=drug_data['id'],
                    defaults=drug_data
                )
                if created:
                    self.stdout.write(f'Created drug: {drug.ten_thuoc}')

            # Create interactions
            for interaction_data in interactions_data:
                try:
                    drug1 = Drug.objects.get(id=interaction_data['drug1_id'])
                    drug2 = Drug.objects.get(id=interaction_data['drug2_id'])
                    
                    interaction, created = DrugInteraction.objects.get_or_create(
                        drug1=drug1,
                        drug2=drug2,
                        defaults={
                            'mechanism': interaction_data['mechanism'],
                            'consequence': interaction_data['consequence'],
                            'management': interaction_data['management'],
                            'severity': interaction_data['severity'],
                        }
                    )
                    if created:
                        self.stdout.write(f'Created interaction: {drug1.ten_thuoc} - {drug2.ten_thuoc}')
                except Drug.DoesNotExist:
                    self.stdout.write(
                        self.style.WARNING(f'Drug not found for interaction: {interaction_data}')
                    )

        self.stdout.write(
            self.style.SUCCESS('Sample data loaded successfully!')
        ) 