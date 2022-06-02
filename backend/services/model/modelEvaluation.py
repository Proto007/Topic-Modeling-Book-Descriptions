import ldaModel
from sklearn.model_selection import GridSearchCV
from sklearn.decomposition import LatentDirichletAllocation
import matplotlib.pyplot as plt

search_params = {'n_components': [10, 15, 20, 25, 30], 'learning_decay': [.5, .7, .9],'random_state':[100]}

# Init the Model
lda = LatentDirichletAllocation()

# Init Grid Search Class
model = GridSearchCV(lda, param_grid=search_params)

# Do the Grid Search
model.fit(data_vectorized)
# Best Model
best_lda_model = model.best_estimator_

# Model Parameters
print("Best Model's Params: ", model.best_params_)

# Log Likelihood Score
print("Best Log Likelihood Score: ", model.best_score_)

# Perplexity
print("Model Perplexity: ", best_lda_model.perplexity(data_vectorized))