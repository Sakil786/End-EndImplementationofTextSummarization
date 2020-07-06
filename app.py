from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
# load the pkgs
from gensim.summarization import summarize
import pickle


app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():
	message = request.form['message']
		
	summary_txt = summarize(message)
	summary_txt


	if request.method == 'POST':
		message = request.form['message']
		
		summary_txt = summarize(message)
		summary_txt
		
	return render_template('result.html',value=summary_txt)



if __name__ == '__main__':
	app.run(debug=True)
