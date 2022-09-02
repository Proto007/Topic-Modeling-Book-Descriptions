# Topic-Modeling-Book-Descriptions
Is it possible to predict a books topic from a given book description? We created a topic model using a book descriptions dataset to find out! 

We used the popular topic modeling technique LDA. If you want to learn more about it, visit https://en.wikipedia.org/wiki/Latent_Dirichlet_allocation. 

Following is a graph that shows log likelyhood score for models with different parameters. We chose 15 topics with a learning decay of 0.6 to maintain a healthy number of topics without sacrificing topic coherence.

![Alt text](/backend/services/model/gridSearch.png?raw=true "gridSearch")

The dataset used in this project can be acquired from https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata
# Installation (may vary based on OS)

1. Clone this repository
2. Create a Python virtual environment and activate it
```
python3 -m venv newvenv
```
3. cd to backend/scripts/model directory
4. Install python dependencies: `pip3 install -r requirements.txt`
5. Train the model by running trainModel.py: `python trainModel.py`
6. Set BENTOML_CONFIG environment variable
```
// Windows:
set BENTOML_CONFIG=./config.yaml
// Linux or Unix:
export BENTOML_CONFIG=./config.yaml
```
7. Start bentoML dev frontend to test post requests: `bentoml serve`
8. Open http://localhost:3001 to see bentoML swagger UI.

# Frontend
1. Change into the frontend folder in a different CLI and install node dependencies: `npm install`
2. Start frontend using `npm start`
3. Open http://localhost:3000 to see frontend simple webapp

# Demo
Here is a demo showing the usage of the frontend webapp:

![Alt text](/demo.gif?raw=true "demo")
