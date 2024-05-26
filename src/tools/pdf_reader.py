from PyPDF2 import PdfReader

def read_pdf(pdfFile : any) -> str:
    raw_text = ""
    for i, page in enumerate(PdfReader(pdfFile).pages):
        raw_text += page.extract_text()
    
    return raw_text