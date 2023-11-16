import pandas as pd
import numpy as np
import cv2
import glob 
import matplotlib.pylab as plt
import time

class DetectPixels:
    def __init__(self, filename):
      self.filename = filename
        
        
    def read_print_image(filename):
        image = cv2.imread(filename)
        
        #To display and show the shape of the image
        #print(f"shape of the image: {(image.shape)}") 
        #fig, ax = plt.subplots(figsize=(10,10))
        #ax.imshow(image)

        return image
    
    def to_grayscale(image):
        # Use the cvtColor() function to grayscale the image 
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
        
        #to display the image
        #window_name='Grayscale Conversion OpenCV'
        #cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
        #cv2.imshow(window_name,img_gray)
        #cv2.waitKey(5000)
        #cv2.destroyAllWindows()
        
        return img_gray

        
    def calculate_white_pixel(image):
        # Flatten the image and create a pandas Series
        pixel_dist = pd.Series(image.flatten(), name='pixel')
        # Create a DataFrame with the 'index' column
        df = pd.DataFrame(pixel_dist)
        non_white_pixel_count = df.loc[(df['pixel'] != 255)]
        white_pixel_count = (len(df['pixel']) - len(non_white_pixel_count))
        white_pixel_percentage = white_pixel_count / len(df['pixel']) *100
        
        print(f"White colour pixel: {round(white_pixel_percentage,3)} %")
        return white_pixel_percentage
    

    def detext_blank_page(percentage):
        if percentage == 100:
            return True
        else:
            return False



filename = "ultrasound.jpg"
white_image = DetectPixels.read_print_image(filename)
image_gray = DetectPixels.to_grayscale(white_image)
percentage = DetectPixels.calculate_white_pixel(image_gray)
DetectPixels.detext_blank_page(percentage)



#Free_Test_Data_1MB_PDF.jpg
#non-text-searchable.jpg