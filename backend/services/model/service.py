import numpy as np
import bentoml
import ldaModel
from bentoml.io import NumpyNdarray, Text


# Load the data_vectorized, vectorizer and lda_model from the disk
data_vectorized=bentoml.sklearn.load_model("data_vectorized:latest")
vectorizer=bentoml.sklearn.load_model("vectorizer:latest")
lda_model=bentoml.sklearn.load_model("ldamodel:latest")
number_of_topics=lda_model.get_params()["n_components"]

# Create a dataframe that can be used for the prediction function
df_topic_keywords = ldaModel.show_topics(vectorizer, lda_model,number_of_topics)

lda_model_runner = bentoml.sklearn.get("ldamodel:latest").to_runner()
svc = bentoml.Service("lda_model_classifier", runners=[lda_model_runner])
@svc.api(input=Text(), output=NumpyNdarray())
def predict(input_series) -> np.ndarray:
    topics = ldaModel.predict(str(input_series), vectorizer, lda_model, df_topic_keywords) 
    topicsArr = np.array(topics)
    return topicsArr
