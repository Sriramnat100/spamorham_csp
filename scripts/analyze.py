#importing packages, pandas to view data, re to look for regular expressions, and sklearn to make preds
import pandas as pd
import re
from sklearn.model_selection import train_test_split, GridSearchCV

from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

#loading dataframe and deleting unwanted columns
df = pd.read_csv('spam.csv', encoding='latin-1')
df.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], axis=1, inplace=True)

#removing any special characters while keeping whitespaces
df['v2'] = df['v2'].apply(lambda x: re.sub('[^A-Za-z0-9\s]+', '', x))

#replacing all the 'spams' with 1s and all the 'hams' with 0s
df['v1'] = df['v1'].replace({'spam': 1, 'ham': 0})

#changing up column names
df.rename(columns={'v1': 'result'}, inplace=True)
df.rename(columns={'v2': 'input'}, inplace=True)

#You could input any of your own text here to see if it is either spam or ham. 


def analyzer(new_text):
    pipeline = Pipeline([
        ('vectorizer', TfidfVectorizer(stop_words='english')),
        ('classifier', LogisticRegression())
    ])

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(df['input'], df['result'], test_size=0.2, random_state=42)

    # Fit the pipeline to the training data
    pipeline.fit(X_train, y_train)

    # Use the pipeline to predict the labels of the test data
    y_pred = pipeline.predict(X_test)

    # Predict the probabilities using proba
    new_text_list = [new_text] # create a list with the single input text
    y_proba = pipeline.predict_proba(new_text_list) # pass the list to the vectorizer
    for i in range(len(new_text_list)):
        return("Probability of ham:", (100*(y_proba[i][0])), "Probability of spam:", (100*(y_proba[i][1])))

