import fitz

def extract_text_by_page(pdf_path):

    doc = fitz.open(pdf_path)

    text_by_page = {}

    for page_index, page in enumerate(doc):

        text_by_page[page_index] = page.get_text()

    return text_by_page