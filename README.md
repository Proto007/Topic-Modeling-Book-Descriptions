# Topic-Modeling-Book-Descriptions
This is an LDA Topic Model trained with a book descriptions dataset. The frontend allows entry of a book description to predict its topic.

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
3. cd to backend/services/model directory
4. Install python dependencies: `pip3 install -r requirements.txt`
5. Train the model by running trainModel.py: `python trainModel.py`
6. Set BENTOML_CONFIG environment variable
```
// Windows:
set BENTOML_CONFIG=./config.yaml
// Linux or Unix:
export BENTOML_CONFIG=./config.yaml
```
1. Start bentoML dev frontend to test post requests: `bentoml serve service.py`
2. Open http://localhost:3001 to see bentoML swagger UI.

# Frontend
1. Change into the frontend folder in a different CLI and install node dependencies: `npm install`
2. Start frontend using `npm start`
3. Open http://localhost:3000 to see frontend simple webapp

# Demo
1. We need to provide the model with a book description. Let's choose description of a book that came out recently. For this demo, we will use the book *Tomorrow, and Tomorrow, and Tomorrow* by Gabrielle Zevin. The description is copied from here: https://www.goodreads.com/book/show/58784475-tomorrow-and-tomorrow-and-tomorrow
![Alt text](/demo/input.jpg?raw=true "demo_input")
2. Clicking **Get Topics** results in the following output:
![Alt text](/demo/output.jpg?raw=true "demo_output")
**The book we used in the demo is labeled with the these genres: Fiction, Contemporary, Romance, Audiobook, Literary Fiction, Historical Fiction, Adult. Based on the output, topics 2, 10, 13 and 4 have the highest frequency. Looking at the words for these high frequency topics, we can infer that the model accurately predicts the topic of the book from it's description.**
# Demo Gif
![Alt text](/demo/demo.gif?raw=true "demo")
