"""
    Author: Sadab Hafiz
    Description: This file contains functions to read and prepare the dataset for the LDA model
"""
#Imports for reading and filtering languages other than English
import pandas as pd
from langdetect import detect

"""
    Read given .csv dataset into a list of strings where each string serves as a book description
    The .csv file provided must have a column called 'description'
    @params:
        fname (string): name of the .csv file being read
    @return:
        A list of strings
"""
def read_data(fname):
    #Read csv into a dataframe
    book_df=pd.read_csv(fname)

    #Create a list of all descriptions from the dataframe
    descriptions=[]
    for each_description in book_df['description']:
        #Add descriptions greater than length 10
        if(len(str(each_description))>10):
            #Filter out languages other than English
            lang=detect(str(each_description))
            if(lang!='en'):
                continue
            descriptions.append(each_description.strip())
    
    return descriptions
