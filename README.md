# project_pdf_sorting




## Module
Split_no_text_pages.py: 
This simple Python script utilizes the PyPDF2 library to remove blank pages from a PDF file. Blank pages are identified by checking if a page contains any text or not. If a page is determined to be blank, it is excluded from the final output PDF.

white_detection.py: 
This Python script utilizes the OpenCV library along with pandas and numpy to detect the percentage of white pixels in grayscale images. The script iterates through a specified directory, processes each image, calculates the percentage of white pixels, and determines whether the image is a blank page based on the white pixel percentage.

- How it works
1. The script defines a class DetectPixels with methods to read and process images, calculate white pixel percentages, detect blank pages, and save the results.
2. The read_cvt_gray_image method reads an image file, converts it to grayscale, and returns the grayscale image.
3. The calculate_white_pixel method flattens the grayscale image, creates a pandas Series, and calculates the percentage of white pixels.
4. The detect_blank_page method determines if an image is blank based on the white pixel percentage.
5. The save_result method prompts the user to select a folder, processes images in the folder, and saves the results in a CSV file.