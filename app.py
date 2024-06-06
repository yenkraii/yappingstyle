from flask import Flask, render_template, request, redirect, url_for
import oauth2 as oauth
import urllib.request
import urllib.parse
import urllib.error
import json

app = Flask(__name__,template_folder="pages") 
  
@app.route("/") 
def mainpage(): 
    return render_template('index.html') 

@app.route("/connect")
def connect():
    return "<h1> TWT API </h1>"

@app.route("/failed")
def failed():
    return "failed"

if __name__ == "__main__":
    app.run(debug=True)