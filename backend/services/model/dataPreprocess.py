"""
    Author: Sadab Hafiz
    Description: This file contains functions to read and prepare the dataset for the LDA model
"""
#Imports for reading and filtering languages other than English
from turtle import pos
import pandas as pd
from langdetect import detect

#Imports for processing the data
import nltk
#Download Wordnet through NLTK in python console:
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet

"""
    Read given .csv dataset into a list of strings where each string serves as a book description
    The .csv file provided must have a column called 'description'
    @params:
        fname (string): name of the .csv file being read
    @return:
        A list of strings
"""
def read_data(fname):
    if not fname:
        return []
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

"""
    This function takes a word and returns the pos tag in a format that is recognized by wordnet lemmatizer
    @params (string): query word
    @return (string): pos tag that is recognizable by wordnet lemmatizer/ empty if the given word is empty or not one of the lemmatized pos
"""
def get_pos_tag(word):
    #Return empty string if query word is invalid
    if not word:
        return ""
    #Get the uppercase of first letter of the pos recognized by nltk's pos_tag function
    tag=nltk.pos_tag([word])[0][1][0].upper()

    #Return approprite wordnet pos tag based on the pag recognized by nltk's pos_tag function
    if(tag=="J"):
        return wordnet.ADJ
    elif(tag=="N"):
        return wordnet.NOUN
    elif(tag=="V"):
        return wordnet.VERB
    elif(tag=="R"):
        return wordnet.ADV
    #Return empty if the given word is not one of the above tags
    return ""