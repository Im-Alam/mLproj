from flask import Flask, render_template, request, url_for, redirect
import pickle
import pandas as pd
import numpy as np


variables =  pickle.load(open('MovieRecommender','rb'))
W = variables['W']
X = variables['X']
B = variables['B']

movie_list = pd.read_csv('MovieData/small_movie_list.csv')

app = Flask(__name__)

@app.route('/')
def index():
    #make data of popular, rending, collaborative filter and pass to renderer.
    return render_template('index.html')


@app.route('/found', methods=['POST'])
def found():
    #Based on data posted by form, find and make data of searched movie.
    return render_template('found.html')


@app.route('/handleClick', methods=["GET"])
def handleClick():
    # Extract associated data from the request
    title = request.args.get('title')
    rating = request.args.get('rating')

    # Construct the data dictionary
    data = {"name": title, 
            "year": "2018", 
            "actor": "Roar Uthaug",
            "lnk": "https://mr.comingsoon.it/imgdb/locandine/235x336/53750.jpg",
            "avg_rating": "4.2",
            "no_rating": "436",
            "crew_id": ["123", "231", "873"]}
    
    # Render the movie.html template with the data
    return render_template('test.html')


@app.route('/movie', methods=['POST'])
def movie():
    #Based on movieId we have to search for all data related to movie and make data
    title = request.args.get('title')
    rating = request.args.get('rating')
    data = {"name":title, 
            "year":"2018", 
            "actor":"Roar will Uthaug",
            "lnk":"https://mr.comingsoon.it/imgdb/locandine/235x336/53750.jpg",
            "avg_rating":"4.2",
            "no_rating": rating,
            "crew_id":["123","231","873"]} 
    #print("Data is:", data)
    return render_template('movie.html', data=data)





if __name__ == '__main__':
    app.run(debug=True)