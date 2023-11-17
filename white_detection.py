import pandas as pd
import numpy as np
import cv2
import glob 
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory 

class DetectPixels:
    def __init__(self, filename=None):
      self.filename = filename
        
        
    def read_cvt_gray_image(self, filename):
        image = cv2.imread(filename)
        
        # Check image files are readable
        #if image is None:
        #    print(f"Error: Unable to read the image at {filename}")
        
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return gray_image
        
    def calculate_white_pixel(self, image):
        # Flatten the image and create a pandas Series
        pixel_dist = pd.Series(image.flatten(), name='pixel')
        # Create a DataFrame with the 'index' column
        df = pd.DataFrame(pixel_dist)
        non_white_pixel_count = df.loc[(df['pixel'] != 255)]
        white_pixel_count = (len(df['pixel']) - len(non_white_pixel_count))
        white_pixel_percentage = white_pixel_count / len(df['pixel']) *100
        return white_pixel_percentage
    

    def detect_blank_page(self, percentage):
        if percentage == 100:
            return True
        else:
            
            return False

    def save_result(self, save_filename):
        # To ask a folder
        Tk().withdraw()
        path = askdirectory(title = "Select a folder")
        walker = os.walk(path)

        outlet = pd.DataFrame(columns=['File Name', 'WhitePix', 'Result', 'Dir_name' ])
        dict_list = []
        for folder, subfoler, files in walker:
            for file in files:
                filepath = os.path.join(folder,file)
                filename = os.path.basename(filepath)
                dirname = os.path.dirname(filepath)
                dirname = os.path.basename(dirname)
                
                image_gray = self.read_cvt_gray_image(filepath)
                percentage = self.calculate_white_pixel(image_gray)
                result = self.detect_blank_page(percentage)
                row_dict = {'File Name': filename, 'WhitePix': percentage, "Result" : result, "Folder Name" : dirname}
                dict_list.append(row_dict)
        outlet = pd.DataFrame.from_dict(dict_list)    
        #outlet.to_string(save_filename)
        outlet.to_csv(save_filename)


        

detect = DetectPixels()
detect.save_result("white_pixel.csv")
