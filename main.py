#Save the file as app.py
from flask import Flask
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def Home():
  return "Hello World"

#Run on command Prompt following commands(Windows):
#   >>cd Desktop/
#   >>cd FlaskFolder
#   >>py -3 -m venv venv
#   >>venv\Scripts\activate
#   >>python app.py