import numpy as np
import bentoml
import ldaModel
from bentoml.io import NumpyNdarray, Text


data_vectorized,vectorizer=ldaModel.get_data_vectorized('books.csv',10, 0.8)
lda_model=ldaModel.create_lda_model(data_vectorized,15)
bentoml.sklearn.save_model("ldaModel", lda_model)
df_topic_keywords = ldaModel.show_topics(vectorizer, lda_model,15)

lda_model_runner = bentoml.sklearn.get("ldaModel:latest").to_runner()
svc = bentoml.Service("lda_model_classifier", runners=[lda_model_runner])

@svc.api(input=Text(), output=NumpyNdarray())
def predict(input_series) -> np.ndarray:
    topics = ldaModel.predict(input_series, vectorizer, lda_model, df_topic_keywords) 
    print(topics)
    topicsArr = np.array(topics)
    return topicsArr
