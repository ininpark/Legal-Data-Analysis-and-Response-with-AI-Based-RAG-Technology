from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from transformers import AutoTokenizer, AutoModel
import torch
import os
import pprint

# PDF 파일 디렉토리 설정
pdf_dir = "D:\\도전학기\\10_generate_law_pdf2"
chunk_size = 1000  # 청킹 크기 설정
chunk_overlap = 200  # 오버랩 설정

# 임베딩 모델 및 토크나이저 로드
model_name = 'sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# PrettyPrinter 설정
pp = pprint.PrettyPrinter(indent=1)

pdf_texts = []
for file_name in os.listdir(pdf_dir):
    if file_name.endswith('.pdf'):
        file_path = os.path.join(pdf_dir, file_name)
        loader = PyPDFLoader(file_path)
        
        # 청킹 설정
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )
        
        # PDF 로드 및 청킹
        pages = loader.load_and_split(text_splitter)
        
        # 청킹된 페이지 수와 각 청크의 길이 확인
        print(f"PDF file: {file_name}, Number of chunks: {len(pages)}")
        for i, page in enumerate(pages):
            print(f"Chunk {i+1} length: {len(page.page_content)}")
        
        # 모든 청크를 리스트에 추가
        for page in pages:
            pdf_texts.append((file_name, page.page_content))

# 첫 번째 청크의 내용과 메타데이터 출력
if pdf_texts:
    print("First chunk content:")
    print(pdf_texts[0][1])
    print("First chunk metadata:")
    print(pages[0].metadata)

# 청킹된 텍스트 예쁘게 출력
for file_name, text in pdf_texts:
    print(f"File: {file_name}")
    pp.pprint(text)

# 임베딩 생성 함수
def generate_embeddings(texts, tokenizer, model):
    embeddings = []
    for text in texts:
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        embeddings.append(outputs.last_hidden_state.mean(dim=1).squeeze().numpy())
    return embeddings

# 청킹된 텍스트만 추출
chunked_texts = [text for _, text in pdf_texts]

# 임베딩 생성
embeddings = generate_embeddings(chunked_texts, tokenizer, model)

# 임베딩 확인
print(f"Generated {len(embeddings)} embeddings.")
print(embeddings[0])  # 첫 번째 임베딩 출력
