# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 14:03:36 2019

@author: gordon.garisch
"""
import os
from glob import glob
from zipfile import ZipFile

class Extractor(object):
    def __init__(self, input_dir, output_dir, temp_dir):
        # Initialize object variables
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.temp_dir = temp_dir

    def extract(self, extract = True, consolidate = True):
        # Set folder locations from object
        report_path = self.output_dir
        temp_path = self.temp_dir
        # Extract function
        if extract:
            for zfn in glob(os.path.join(self.input_dir, '*.zip')):
                # Lookp through zip files in input location
                
               
    
                # Create folder if it does not exist
                if not os.path.exists(report_path):
                    os.makedirs(report_path)
    
                count = 0
                # Extract zip file 
                with ZipFile(zfn, 'r') as z:
                    for fn in z.namelist():
                        efn = z.extract(fn, temp_path)
                        count += 1
        
                print('extracted {} reports to {}'.format(count, report_path))
        
        if consolidate:
            # Loop through folders, searching for .txt files to consolidate
            for subdir, dirs, files in os.walk(temp_path):
                for txtfl in glob(os.path.join(temp_path, '*.txt')):
                    finp = open(txtfl,"r")
                    foutp = open(os.path.join(report_path,'output.txt'),"a+")
                    foutp.write(finp.read())                


if '__main__' == __name__:    
    # =============================================================================
    # Set inpput, output and temp file locations
    # =============================================================================
    input_dir = ('C:\\Users\\gordon.garisch\\Documents\\Projects\\Stevens\\fe595\\FE595_Assignment3\\data\\')
    output_dir = os.path.join(input_dir,'output')
    temp_dir = os.path.join(input_dir,'temp')
    # =============================================================================
    # Create extractor object
    # =============================================================================
    extractor = Extractor(input_dir, output_dir,temp_dir)
    # =============================================================================
    # Extract function
    # =============================================================================
    extractor.extract(extract = False)