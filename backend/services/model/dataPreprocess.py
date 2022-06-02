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
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#Download Wordnet through NLTK in python console
nltk.download('wordnet')


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
    Returns the pos tag of given word in a format that is recognized by wordnet lemmatizer
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

"""
    Return lemmatized form of given word if it is a noun, verb, adjective or adverb.
    @params (string): query word
    @return (string): lemmatized word if it is one of the valid pos tags/ returns the word itself if it is empty or not a valid pos tag
"""
def lemmatize(word):
    #Return the word itself if its empty
    if not word:
        return word
    #Initialize the lemmatizer
    lemmatizer=WordNetLemmatizer()
    #Get the pos tag for the word
    pos_tag=get_pos_tag(word)
    #If the pos tag is not valid, return the word itself
    if not pos_tag:
        return word
    #Return the lemmatized form of the word
    return lemmatizer.lemmatize(word,pos_tag)

"""
    Updates passed list of strings into a list of lists where each sublist is a list of words after preprocessing
    Preprocessing includes tokenizing(using nltk), removing stopwords, lemmatizing, casefolding
    @param (list of strings): list of descriptions from the dataset
    @result: param list is updated into a list of lists where each sublist is a list of strings
"""
def preprocess(descriptions):
    #Get the stopwords_list from nltk
    stopwords_list=stopwords.words('english')

    #Tokenize, lemmatize, remove stopwords, remove numeric words, remove endline
    for i in range(len(descriptions)):
        #Tokenize the words from each description using nltk's tokenizer
        descriptions[i]=word_tokenize(descriptions[i])
        #List used to keep track of words after processing
        processed_description=[]
        for word in descriptions[i]:
            #Filter out the stopwords
            if word not in stopwords_list:
                #Filter out words that are not greater than length of 2 chars and numeric words
                if((len(word)>2) & (not word.isnumeric())):
                    #Lemmatize the words, remove endline chars and casefold words to lowercase
                    word=lemmatize(word.lower().strip())
                    processed_description.append(word)
        #Update the curr index of descriptions with cleaned list of words
        descriptions[i]=processed_description