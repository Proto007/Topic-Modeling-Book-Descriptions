"""
    Author: Sadab Hafiz
    Description: This file contains functions evaluate LDA models and find best LDA model using different parameters.
"""
# Import necessary functions and modules
from ldaModel import get_data_vectorized
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import LatentDirichletAllocation
import matplotlib.pyplot as plt

"""
    Global Variables that are used throughout. The dataset and minimum doc-word frequency can be changed to try different dataset/configuration.
"""
data_vectorized,vectorizer=get_data_vectorized('books.csv',10,0.8)

"""
    These parameters will be applied during grid search to find the model with best preplexity, log likelihood score and parameters.
    Can be changed to test specific parameters
"""
search_params = {'n_components': [10,11,12,13,14,15], 
                'learning_decay': [.5,.6,.7,.8,.9],
                'random_state':[100], 
                'n_jobs' :[-1], 
                'learning_method':['online']}

"""
    Used to create the evaluation graph
"""
n_components= [10,11,12,13,14,15]

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

"""
    Get the best lda model found in passed grid search result
    @params:
        grid_search_models: result of doing grid search
    @return:
        best_lda_model(LatentDirichletAllocation): best lda model based on grid search

"""
def get_best_lda(grid_search_models):
    return grid_search_models.best_estimator_

"""
    Create a graph showing the result of grid search. THIS FUNCTION DEPENDS ON GLOBAL VARIABLES.
    @params:
        grid_search_models: result of doing grid search
    @result: 'gridSearch.png' created showing the log_likelihood based on the number of topics
    @return: none
"""
def evaluation_graph(grid_search_models):
    # Get the log likelihood based on the learning decays
    log_likelyhoods_5 = [round(grid_search_models.cv_results_['mean_test_score'][index]) for index, gscore in enumerate(grid_search_models.cv_results_['params']) if gscore['learning_decay']==0.5]
    log_likelyhoods_6 = [round(grid_search_models.cv_results_['mean_test_score'][index]) for index, gscore in enumerate(grid_search_models.cv_results_['params']) if gscore['learning_decay']==0.6]
    log_likelyhoods_7 = [round(grid_search_models.cv_results_['mean_test_score'][index]) for index, gscore in enumerate(grid_search_models.cv_results_['params']) if gscore['learning_decay']==0.7]
    log_likelyhoods_8 = [round(grid_search_models.cv_results_['mean_test_score'][index]) for index, gscore in enumerate(grid_search_models.cv_results_['params']) if gscore['learning_decay']==0.8]
    log_likelyhoods_9 = [round(grid_search_models.cv_results_['mean_test_score'][index]) for index, gscore in enumerate(grid_search_models.cv_results_['params']) if gscore['learning_decay']==0.9]
    # Create graph showing log likelihood for the learning decays over the number of topics
    plt.figure(figsize=(12, 8))
    plt.plot(n_components, log_likelyhoods_5, label='0.5')
    plt.plot(n_components, log_likelyhoods_6, label='0.6')
    plt.plot(n_components, log_likelyhoods_7, label='0.7')
    plt.plot(n_components, log_likelyhoods_8, label='0.8')
    plt.plot(n_components, log_likelyhoods_9, label='0.9')
    # Label the graph
    plt.title("Choosing Optimal LDA Model")
    plt.xlabel("Num Topics")
    plt.ylabel("Log Likelyhood Scores")
    plt.legend(title='Learning decay', loc='best')
    # Save the graph
    plt.savefig('gridSearch.png')

"""
    Code used to perform grid search and save the graph
"""
grid_search=lda_grid_search()
best_lda=get_best_lda(grid_search)

# Print the parameters resulting in best model
print("Best Model's Params: ", grid_search.best_params_)

# Print the log likelihood of the best model
print("Best Log Likelihood Score: ", grid_search.best_score_)

# Print the perplexity of the best model
print("Model Perplexity: ", best_lda.perplexity(data_vectorized))

# Create graph to show result of grid_search
evaluation_graph(grid_search)

"""
    The output for the above code:
        Best Model's Params:  {'learning_decay': 0.6, 'learning_method': 'online', 'n_components': 10, 'n_jobs': -1, 'random_state': 100}
        Best Log Likelihood Score:  -305291.73704079085
        Model Perplexity:  2222.1323464111842
"""