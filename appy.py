from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path,join(dirname(__file__), '.env')
Load_dotenv(dotenv_path)

MONGODB_URI = os.environ.get("MONGODB_URI")
DB_NAME = os.environ.get("DB_NAME")


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['name_give']
    doc = {
        'name' : name_receive,
        'comment' : comment_receive
    }
    db.fanmessages.insert_one(doc)
    return jsonify({'msg':'POST request!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    return jsonify({'msg':'GET request!'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)