from datasets import load_dataset
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import re
import os

# Hugging Face에서 데이터셋 불러오기
dataset = load_dataset("joonhok-exo-ai/korean_law_open_data_precedents", download_mode="force_redownload")

# 처음 5000개의 항목만 변환 (테스트를 위해 5000개로 제한)
sample_data = dataset['train'].select(range(10000))

def convert_to_detailed_structure(full_text):
    # 【】 안의 내용을 키로 하고, 나머지 텍스트를 값으로 하는 딕셔너리 생성
    pattern = r'【(.*?)】'
    keys = re.findall(pattern, full_text)
    values = re.split(pattern, full_text)[1:]
    
    section_dict = {}
    for i in range(0, len(values), 2):
        key = keys[i//2]
        value = values[i+1].replace('\n', ' ').strip()
        section_dict[key] = value
    
    return section_dict

def create_pdf(case_data, font_path, output_dir):
    # PDF 파일 이름
    pdf_file = os.path.join(output_dir, f"{case_data['판례정보일련번호']}.pdf")
    
    # PDF 문서 설정
    doc = SimpleDocTemplate(pdf_file, pagesize=A4, rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20)
    styles = getSampleStyleSheet()
    
    # 한글 폰트 설정
    pdfmetrics.registerFont(TTFont('NotoSansKR', font_path))
    normal_style = ParagraphStyle(name='Normal', fontName='NotoSansKR', fontSize=10)
    heading_style = ParagraphStyle(name='Heading1', fontName='NotoSansKR', fontSize=10, spaceAfter=6)

    elements = []

    # Case ID 추가
    elements.append(Paragraph(f"Case ID: {case_data['판례정보일련번호']}", heading_style))
    elements.append(Spacer(1, 12))

    # 나머지 데이터 추가
    for key, value in case_data.items():
        if key == "참조판례":  # 참조판례가 존재하는 경우에만 추가
            if value:
                elements.append(Paragraph(f"{key}: {', '.join(value)}", normal_style))
                elements.append(Spacer(1, 12))
        elif key == "전문":  # 전문 내용을 상세 구분으로 나누기
            detailed_sections = convert_to_detailed_structure(value)
            for section, text in detailed_sections.items():
                elements.append(Paragraph(f"{section}: {text}", normal_style))
                elements.append(Spacer(1, 12))
        else:
            if isinstance(value, list):  # 리스트 타입 처리
                value = ', '.join(value)
            elif isinstance(value, dict):  # 딕셔너리 타입 처리
                value = '<br/>'.join([f"{k}: {v}" for k, v in value.items()])
            elements.append(Paragraph(f"{key}: {value}", normal_style))
            elements.append(Spacer(1, 12))

    # PDF 저장
    doc.build(elements)
    return pdf_file

# 폰트 파일 경로 설정
font_path = "C:\\Users\\OWNER\\inhye\\Natural_language\\인혜,민정_도전학기\\Noto_Sans_KR\\NotoSansKR-VariableFont_wght.ttf"
# 저장 디렉토리 설정
output_dir = "D:\\pdfs"

# 저장 디렉토리 존재 확인 및 생성
os.makedirs(output_dir, exist_ok=True)

# 각 판례 데이터를 PDF로 변환
for case in sample_data:
    pdf_file = create_pdf(case, font_path, output_dir)
    print(f"Created PDF: {pdf_file}")
