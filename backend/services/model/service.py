import numpy as np
import ldaModel
import bentoml

from bentoml.io import NumpyNdarray


data_vectorized,vectorizer=ldaModel.get_data_vectorized('books.csv',10,0.8)
lda_model=ldaModel.create_lda_model(data_vectorized,15)
bentoml.sklearn.save_model("lda_model", lda_model)

lda_model_runner = bentoml.sklearn.get("lda_model:latest").to_runner()

svc = bentoml.Service("lda_model_classifier", runners=[lda_model_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_series: np.ndarray) -> np.ndarray:
    return lda_model_runner.predict.run(input_series)
