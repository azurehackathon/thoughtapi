from flask import Flask
import requests
import random 
import json
app = Flask(__name__)

q = None
with open("quotes.json") as f:
    q = json.load(f)
@app.route('/')
def hello():
    print "type is " + str(type(q[random.randint(0,len(q)-1)]))
    return q[random.randint(0,len(q)-1)]["quoteText"]



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=3000)