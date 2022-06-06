"""
    Author: Sadab Hafiz
    Description: This file contains functions to create,visualize and use an LDA model.
"""
# Import functions for data reading and cleaning
import dataPreprocess as dp

# Import sklearn functions for LDA model
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

# Imports to visualize the LDA model
import pyLDAvis
import pyLDAvis.sklearn
import numpy as np
import pandas as pd

"""
    Create doc-word matrix from given dataset using a CountVectorizer
    @params:
        dataset_csv (string): name of training dataset csv file, file must have column named "description"
        minimum_df (int): words that occur atleast minimum_df times is considered for the model
        maximum_df (float): words that occur more than this frequency is ignored
    @return:
        data_vectorized: doc-word matrix
        vectorizer: CountVectorizer class instance used to create doc-word matrix
"""
def get_data_vectorized(dataset_csv, minimum_df, maximum_df):
    #Initialize CountVectorizer with configurations to only consider words that occur atleast given minimum_df times
    vectorizer = CountVectorizer(analyzer='word',
                             min_df=minimum_df,
                             max_df=maximum_df,                # Ignore words more than this frequency
                             stop_words='english',             # remove stop words
                             lowercase=True,                   # convert all words to lowercase
                             token_pattern='[a-zA-Z]{3,}',     # words should be atleast 3 chars long
                             )
    #Read the provided dataset
    descriptions_data=dp.read_data(dataset_csv)
    #Tokenize, remove stopwords, case-fold, lemmatize the data
    dp.preprocess(descriptions_data)
    #Create doc-word matrix which is the input for the LDA model
    data_vectorized=vectorizer.fit_transform(descriptions_data)
    return data_vectorized,vectorizer

"""
    Creates lda_model with given number_of_topics and doc-word matrix from dataset
    @params:
        data_vectorized: doc-word matrix created from the dataset
        num_of_topics (int): number of topics that are generated by the lda model
    @return:
        lda_model (LatentDirichletAllocation): lda model
"""
def create_lda_model(data_vectorized,num_of_topics):
    #Initialize an LDA model with configurations
    lda_model = LatentDirichletAllocation(n_components=num_of_topics,         # Set number of topics to given number
                                        max_iter=10,                          # Max learning iterations
                                        learning_method='online',             # Online method is faster for large datasets
                                        random_state=100,                     # Random state to reproduce same topics
                                        batch_size=128,                       # Documents in each learning iteration
                                        evaluate_every = -1,                  # compute perplexity every n iters, default: Don't
                                        n_jobs = -1,                          # Use all available CPUs
                                        learning_decay=0.6                    # Best learning decay based on log likelihood scored
                                        )
    #Create an LDA model with the given dataset
    lda_model.fit_transform(data_vectorized)
    #Return the LDA model, vectorizer and the doc-word matrix
    return lda_model

"""
    Create "model.html" to show the topics created by the given LDA model
    @params:
        lda_model (LatentDirichletAllocation): lda model
        data_vectorized: doc-word matrix
        vectorizer: CountVectorizer class instance used to create doc-word matrix
    @output:
        model.html (file): model visualization
"""
def visualize_lda_model(lda_model,data_vectorized,vectorizer):
    #Prepare the visualization
    visualization = pyLDAvis.sklearn.prepare(lda_model, data_vectorized, vectorizer, mds='tsne')
    #Save the visualization as 'model.html'
    try:
        pyLDAvis.save_html(visualization,'model.html')
    #Log error in visualization creation
    except:
        print("Failed to create visualization")

"""
    Returns the perplexity score of the provided LDA model
    @params:
        lda_model (LatentDirichletAllocation): lda model
        data_vectorized: doc-word matrix
    @returns:
        perplexity(float): the perplexity of the provided lda model on provided dataset
"""
def get_perplexity(lda_model,data_vectorized):
    lda_model.perplexity(data_vectorized)

"""
    Returns and saves a dataframe with top specified number words for each topic in the given LDA model and vectorizer
    @param:
        lda_model (LatentDirichletAllocation): lda model
        vectorizer: CountVectorizer class instance used to create doc-word matrix
        num(int): number of top words in dataframe for each topic
    @return:
        topic_keywords(pandas dataframe): dataframe is also saved as 'topic_words.csv' 
"""
def show_topics(vectorizer, lda_model, num):
    #  Np array of the feature names in passed vectorizer
    keywords = np.array(vectorizer.get_feature_names())
    topic_keywords = []
    # extract the top words of each topic from the given LDA model
    for topic_weights in lda_model.components_:
        # Sort and get top words based on parameter number
        top_keyword_locs = (-topic_weights).argsort()[:num]
        # Add topwords to list
        topic_keywords.append(keywords.take(top_keyword_locs))
    # Save the topic distribution as a pandas csv
    df_topic_keywords = pd.DataFrame(topic_keywords)
    # Word number
    df_topic_keywords.columns = ['Word '+str(i) for i in range(df_topic_keywords.shape[1])]
    # Topic number
    df_topic_keywords.index = ['Topic '+str(i) for i in range(df_topic_keywords.shape[0])]
    # Save the dataframe
    df_topic_keywords.to_csv("topic_words.csv",index=False)
    return df_topic_keywords

"""
    Predits the topic for the given string using the passed lda_model and returns topic keywords and topic probabilities for each topic
    @params:
        query_description (string): query description
        lda_model (LatentDirichletAllocation): lda model
        vectorizer: CountVectorizer class instance used to create doc-word matrix
        df_topic_keywords (pandas dataframe): dataframe with top words for each topic
    @return:
        topic_distribution (2d list[list of strings, float]): Contains keywords for each topic and the frequency of the topic in query description
"""
def predict(query_description, vectorizer,lda_model,df_topic_keywords):
    # Return empty lists if the input is invalid
    if not query_description:
        print("invalid input")
        return [],[]
    # Clean the query_description and prepare it for CountVectorizer
    dp.preprocess_single(query_description)
    query_description=[query_description]
    # Vectorize the query_description to prepare it for LDA model
    query_description= vectorizer.transform(query_description)

    # Check the topic of the query_description using the passed LDA model
    topic_probability_scores = lda_model.transform(query_description)
    # Get the top words for the each topics
    topics_list=df_topic_keywords.values.tolist()
    # Append the topic keywords and probability of all topics into an array 
    topic_distribution=[]
    for i in range(len(topics_list)):
        topic_distribution.append([topics_list[i],topic_probability_scores[0][i]])
    # Sort the topics based on the frequency
    topic_distribution.sort(key=lambda row:(row[1]), reverse=True)
    return topic_distribution

"""
    Creating an LDA model with best parameters predicted by grid search
"""
# data_vectorized,vectorizer=get_data_vectorized('books.csv',10,0.8)
# lda_model=create_lda_model(data_vectorized,15)
# visualize_lda_model(lda_model,data_vectorized,vectorizer)
# df_topic_keywords = show_topics(vectorizer, lda_model,15)
"""
    Example code showing how to predict the probability of given text using the LDA model
"""
# probability_scores=predict("As a third-year Ph.D. candidate, Olive Smith doesn't believe in lasting romantic relationships--but her best friend does, and that's what got her into this situation. Convincing Anh that Olive is dating and well on her way to a happily ever after was always going to take more than hand-wavy Jedi mind tricks: Scientists require proof. So, like any self-respecting biologist, Olive panics and kisses the first man she sees. That man is none other than Adam Carlsen, a young hotshot professor--and well-known ass. Which is why Olive is positively floored when Stanford's reigning lab tyrant agrees to keep her charade a secret and be her fake boyfriend. But when a big science conference goes haywire, putting Olive's career on the Bunsen burner, Adam surprises her again with his unyielding support and even more unyielding... six-pack abs. Suddenly their little experiment feels dangerously close to combustion. And Olive discovers that the only thing more complicated than a hypothesis on love is putting her own heart under the microscope.",vectorizer,lda_model,df_topic_keywords)
# print(probability_scores)

