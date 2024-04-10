from pypdf import PdfReader


def load_pdf(file):
    """
    This function takes a file path and returns a PdfReader object.

    Parameters:
    file_path (str): The path to the PDF file, in the local directory.

    Returns:
    tuple: A tuple containing the number of pages and the extracted text.
    """

    try:
        # creating a pdf reader object
        reader = PdfReader(file)
        text = ''
        page_count = len(reader.pages)
        for page in range(page_count):
            text += reader.pages[page].extract_text()
        return page_count, text
    except Exception as e:
        print(f"Error parsing PDF: {e}")
        return None

page_count, text = load_pdf('PDFs/Selected_OneNYC_Summary.pdf')
print(f"{page_count} pages")
print(text)