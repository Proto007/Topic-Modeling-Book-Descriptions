# Import functions for data reading and cleaning
import dataPreprocess as dp

# Import sklearn functions for LDA model
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

# Imports to visualize the LDA model
import pyLDAvis
import pyLDAvis.sklearn

"""
    Creates vectorizer and lda_model with given .csv dataset and number of topics
    @params:
        dataset_csv (string): name of training dataset csv file, file must have column named "description"
        num_of_topics (int): number of topics that are generated by the lda model
    @return:
        lda_model (LatentDirichletAllocation): lda model
        data_vectorized: doc-word matrix
        vectorizer: CountVectorizer class instance used to create doc-word matrix
"""
def create_lda_model(dataset_csv,num_of_topics):
    #Initialize CountVectorizer with configurations to only consider words that occur atleast 10 times
    vectorizer = CountVectorizer(analyzer='word',min_df=10)
    #Read the provided dataset
    descriptions_data=dp.read_data(dataset_csv)
    #Tokenize, remove stopwords, case-fold, lemmatize the data
    dp.preprocess(descriptions_data)
    #Create doc-word matrix which is the input for the LDA model
    data_vectorized=vectorizer.fit_transform(descriptions_data)
    #Initialize an LDA model with configurations
    lda_model = LatentDirichletAllocation(n_components=num_of_topics,         # Set number of topics to given number
                                        max_iter=10,                          # Max learning iterations
                                        learning_method='online',             # Online method is faster for large datasets
                                        random_state=100,                     # Random state to reproduce same topics
                                        batch_size=128,                       # Documents in each learning iteration
                                        evaluate_every = -1,                  # compute perplexity every n iters, default: Don't
                                        n_jobs = -1,                          # Use all available CPUs
                                        )
    #Create an LDA model with the given dataset
    lda_model.fit_transform(data_vectorized)
    #Return the LDA model, vectorizer and the doc-word matrix
    return lda_model,data_vectorized,vectorizer

def visualize_lda_model(lda_model,data_vectorized,vectorizer):
    visualization = pyLDAvis.sklearn.prepare(lda_model, data_vectorized, vectorizer, mds='tsne')
    try:
        pyLDAvis.save_html(visualization,'model.html')
    except:
        print("Failed to create visualization")


# Example Function Call to create a 10 topic model and save a visualization
#lda_model,data_vectorized,vectorizer=create_lda_model('books.csv',10)
#visualize_lda_model(lda_model,data_vectorized,vectorizer)