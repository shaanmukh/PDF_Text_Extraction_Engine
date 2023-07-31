import PyPDF2
import re

def extract_text(pdf_path, txt_path):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        text = ""

        for page_num in range(len(pdf_reader.pages)):
   
            page = pdf_reader.pages[page_num]

            page_text = page.extract_text()

            page_text = re.sub(r'[^\w\s]+', '', page_text)

            text += page_text + '\n'
            
            print(f"Length of text string: {len(text)}")

            print(f"Page text:\n{page_text}\n")

    with open(txt_path, 'w', encoding='utf-8') as txt_file:
        txt_file.write(text)

extract_text('test1.pdf', 'example.txt')