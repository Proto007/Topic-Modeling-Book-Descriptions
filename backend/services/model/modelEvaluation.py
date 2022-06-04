from ldaModel import get_data_vectorized
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import LatentDirichletAllocation
import matplotlib.pyplot as plt

"""
    Global Variables that are used throughout. The dataset and minimum doc-word frequency can be changed to try different dataset/configuration.
"""
data_vectorized,vectorizer=get_data_vectorized('books.csv',10)

"""
    These parameters will be applied during grid search to find the model with best preplexity, log likelihood score and parameters.
    Can be changed to test specific parameters
"""
search_params = {'n_components': [10,11,12,13,14], 
                'learning_decay': [.5,.6,.7,.8,.9],
                'random_state':[100], 
                'n_jobs' :[-1], 
                'learning_method':['online']}

"""
    Used to create the evaluation graph
"""
n_components= [10,11,12,13,14]

"""
    Uses passed dataset and search params to return the result of grid search
    @params:
        search_params (dictionary): parameters that are used in grid search
        data_vectorized: doc-word matrix
    @return:
        models: data acquired from gridsearch (running the lda model using all possible search params)
"""
def lda_grid_search(data_vectorized=data_vectorized,search_params=search_params):
    # Initialize the LDA model
    lda = LatentDirichletAllocation()

    # Initialize grid search with given lda model and search params
    models = GridSearchCV(lda, param_grid=search_params)

    # Perform grid search on the given doc-word matrix
    models.fit(data_vectorized)
    
    return models