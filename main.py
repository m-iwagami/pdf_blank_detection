import PyPDF2




def split_no_text_page(pdf_file):
    # Create a PDF object
    pdf = PyPDF2.PdfReader(pdf_file)

    # Create a new PDF object to store the pages without the blank page
    blank_page_pdf = PyPDF2.PdfWriter()
    number_of_pages = len(pdf.pages)

    # Iterate through each page in the PDF
    for page_num in range(number_of_pages):
        page = pdf.pages[page_num]
        text = page.extract_text()

        # Check if the page is blank (contains no text)
        if (len(text) == 0):
            blank_page_pdf.add_page(page)    # Add the blank page to the new PDF
            continue 
        
    # Save the new PDF to a file
    with open('output.pdf', 'wb') as output_file:
        blank_page_pdf.write(output_file)

if __name__ == '__main__':
    with open('Free_Test_Data_1MB_PDF.pdf', 'rb') as pdf_file:
        split_no_text_page(pdf_file)

