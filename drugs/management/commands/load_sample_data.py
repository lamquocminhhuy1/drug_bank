from django.core.management.base import BaseCommand
from django.utils import timezone
from drugs.models import Drug, DrugInteraction


class Command(BaseCommand):
    help = 'Load sample drug and interaction data'

    def handle(self, *args, **options):
        self.stdout.write('Loading sample data...')

        # Create sample drugs
        drugs_data = [
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
                'sys_id': '00124b5dc37b121065eb3fac05013175',
                'sys_created_by': 'lamquocminhhuy',
                'sys_updated_by': 'lamquocminhhuy',
                'sys_mod_count': '1',
                'sys_tags': '',
            },
            {
                'id': 'VN-001-001',
                'ten_thuoc': 'Itraconazol',
                'hoat_chat': 'Itraconazole',
                'phan_loai': 'Thuốc kê đơn',
                'nhom_thuoc': 'Thuốc kháng nấm',
                'nuoc_dk': 'Việt Nam',
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Itraconazol',
                'source_pdf': '',
                'meta_data': '',
                'sys_id': '00124b5dc37b121065eb3fac05013176',
                'sys_created_by': 'system',
                'sys_updated_by': 'system',
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
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Dabigatran',
                'source_pdf': '',
                'meta_data': '',
                'sys_id': '00124b5dc37b121065eb3fac05013177',
                'sys_created_by': 'system',
                'sys_updated_by': 'system',
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
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Aceclofenac',
                'source_pdf': '',
                'meta_data': '',
                'sys_id': '00124b5dc37b121065eb3fac05013178',
                'sys_created_by': 'system',
                'sys_updated_by': 'system',
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
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Ketorolac',
                'source_pdf': '',
                'meta_data': '',
                'sys_id': '00124b5dc37b121065eb3fac05013179',
                'sys_created_by': 'system',
                'sys_updated_by': 'system',
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
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Tramadol',
                'source_pdf': '',
                'meta_data': '',
                'sys_id': '00124b5dc37b121065eb3fac05013180',
                'sys_created_by': 'system',
                'sys_updated_by': 'system',
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
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Warfarin',
                'source_pdf': '',
                'meta_data': '',
                'sys_id': '00124b5dc37b121065eb3fac05013181',
                'sys_created_by': 'system',
                'sys_updated_by': 'system',
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
                'source_data': 'https://drugbank.vn/services/drugbank/api/public/thuoc?tenThuoc=Aspirin',
                'source_pdf': '',
                'meta_data': '',
                'sys_id': '00124b5dc37b121065eb3fac05013182',
                'sys_created_by': 'system',
                'sys_updated_by': 'system',
                'sys_mod_count': '1',
                'sys_tags': '',
            },
        ]

        # Create drugs
        created_drugs = {}
        for drug_data in drugs_data:
            drug, created = Drug.objects.get_or_create(
                id=drug_data['id'],
                defaults=drug_data
            )
            created_drugs[drug.id] = drug
            if created:
                self.stdout.write(f'Created drug: {drug.ten_thuoc}')
            else:
                self.stdout.write(f'Drug already exists: {drug.ten_thuoc}')

        # Create sample interactions
        interactions_data = [
            {
                'drug1_id': 'VN-001-001',  # Itraconazol
                'drug2_id': 'VN-002-001',  # Dabigatran
                'mechanism': 'Itraconazol ức chế CYP3A4 mạnh làm giảm chuyển hóa của dabigatran',
                'consequence': 'Tăng nồng độ dabigatran trong huyết thanh, tăng nguy cơ xuất huyết nghiêm trọng',
                'management': 'Chống chỉ định phối hợp. Cân nhắc thay đổi sang các thuốc kháng nấm khác ít có nguy cơ tương tác hơn.',
                'severity': 'contraindicated',
            },
            {
                'drug1_id': 'VN-003-001',  # Aceclofenac
                'drug2_id': 'VN-004-001',  # Ketorolac
                'mechanism': 'Hiệp đồng tác dụng kích ứng đường tiêu hóa',
                'consequence': 'Tăng nguy cơ xuất huyết tiêu hóa nghiêm trọng (sử dụng đồng thời ketorolac với 1 NSAID khác làm tăng nguy cơ xuất huyết tiêu hóa gấp 5 lần so với phối hợp 2 NSAID khác)',
                'management': 'Chống chỉ định phối hợp. Cần đặc biệt lưu ý nguy cơ tương tác trong trường hợp giảm đau hậu phẫu.',
                'severity': 'contraindicated',
            },
            {
                'drug1_id': 'VN-005-001',  # Tramadol
                'drug2_id': 'VN-001-001',  # Itraconazol
                'mechanism': 'Itraconazol ức chế CYP3A4 làm giảm chuyển hóa của tramadol',
                'consequence': 'Tăng nồng độ tramadol trong huyết thanh, tăng nguy cơ tác dụng không mong muốn (buồn nôn, chóng mặt, suy hô hấp)',
                'management': 'Theo dõi chặt chẽ bệnh nhân khi sử dụng đồng thời. Cân nhắc giảm liều tramadol.',
                'severity': 'major',
            },
            {
                'drug1_id': 'VN-002-001',  # Dabigatran
                'drug2_id': 'VN-004-001',  # Ketorolac
                'mechanism': 'Hiệp đồng tác dụng chống đông máu',
                'consequence': 'Tăng nguy cơ xuất huyết nghiêm trọng',
                'management': 'Tránh sử dụng đồng thời. Nếu cần thiết, theo dõi chặt chẽ các dấu hiệu xuất huyết.',
                'severity': 'major',
            },
            {
                'drug1_id': 'VN-003-001',  # Aceclofenac
                'drug2_id': 'VN-005-001',  # Tramadol
                'mechanism': 'Tương tác dược động học nhẹ',
                'consequence': 'Có thể tăng tác dụng giảm đau',
                'management': 'Theo dõi bệnh nhân khi sử dụng đồng thời.',
                'severity': 'moderate',
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
        ]

        # Create interactions
        for interaction_data in interactions_data:
            drug1 = created_drugs[interaction_data['drug1_id']]
            drug2 = created_drugs[interaction_data['drug2_id']]
            
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
            else:
                self.stdout.write(f'Interaction already exists: {drug1.ten_thuoc} - {drug2.ten_thuoc}')

        self.stdout.write(
            self.style.SUCCESS('Successfully loaded sample data!')
        ) 