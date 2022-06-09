# Topic-Modeling-Book-Descriptions

> **_NOTE:_** The frontend of the application is not finished due to issues with BentoML Heroku deployment.

The dataset used in this project can be acquired from https://www.kaggle.com/datasets/dylanjcastillo/7k-books-with-metadata
# Installation (may vary based on OS)

1. Clone this repository
2. Create a Python virtual environment in the repo:
```
python3 -m venv newvenv
```

3. Activate it with `./Topic-Modeling-Book-Descriptions/bin/activate`
4. cd to backend/scripts/model directory
5. Install python dependencies: `pip3 install -r requirements.txt`
6. Train the model by running trainModel.py: `python trainModel.py`
7. Start bentoML dev frontend to test post requests: `bentoml serve`
8. Open localhost to see bentoML swagger UI.

#Frontend (reach + not finished yet)
1. Change into the frontend folder and install node dependencies: `npm install`
2. Start frontend using `npm start`
3. Open localhost to see frontend simple webapp

