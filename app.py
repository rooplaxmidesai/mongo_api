#!/usr/bin/env python

#import necessary libraries
#pip install flask
from flask import Flask,render_template,request
#import os
from flask_pymongo import PyMongo
import datetime


#create instamce of the application
#export FLASK_APP=flask-app

app  = Flask(__name__)


app.config['MONGO_URI'] = "mongodb://localhost:27017/shows_db"

mongo = PyMongo(app)

tv_shows = mongo.db.tv_shows


#decorator
@app.route("/")
def index():
    all_shows = list(tv_shows.find())
    print(all_shows)
    return render_template("index.html",data=all_shows)

@app.route("/insert",methods=['GET','POST'])
def insert_tvshow():
    if request.method=='GET':
        return render_template("tvshow.html")
    elif request.method=='POST':
        #CREATE
        # dictionary that represents the document
        showname = request.form["sname"]
        seasons = request.form["seasons"]
        duration = request.form["duration"]
        year = request.form["year"]
        post_data = {'name':showname,
                'seasons': seasons,
                'duration':duration,
                'year':year,
                'date_added': datetime.datetime.utcnow()
                }

        tv_shows.insert_one(post_data)
        return "<p> " + showname + " Tv show added</p>"


@app.route("/update/<tvshow_name>",methods=['GET','POST'])
def update_tvshow(tvshow_name):
    if request.method=='GET':
        show = tv_shows.find_one({'name': tvshow_name})
        print(show)
        return render_template("tvshow_update.html",data=show)
    elif request.method=='POST':
        #UPDATE
        filter = {'name': tvshow_name}

        seasons = request.form["seasons"]
        duration = request.form["duration"]
        year = request.form["year"]

        # Values to be updated.
        newvalues = { "$set": { 'year': year,'seasons':seasons,'duration':duration } }
    
        # Using update_one() method for single 
        tv_shows.update_one(filter, newvalues) 

        return "<p>TV show " + tvshow_name + " updated</p>"


@app.route("/delete/<tvshow_name>")
def delete_tvshow(tvshow_name):
    #DELETE
    tv_shows.delete_one({'name':tvshow_name})
    return "<p>TV show" + tvshow_name + " deleted</p>"

if __name__ == "__main__":
    app.run(debug=True)


