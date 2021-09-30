from flask import Flask,redirect,url_for,render_template,request
import numpy as np
from sklearn.preprocessing import StandardScaler
import pickle
from Validation import form_response


sc=StandardScaler()

app = Flask(__name__)


# Pkl_Filename = "Pickle_RL_Model.pkl"
# with open(Pkl_Filename, 'rb') as file:  
#     model = pickle.load(file)


@app.route("/",methods=['POST','GET'])
def register():
	if request.method=='POST':
		if request.form:
			dict_req = dict(request.form)
			print(dict_req)	
			response = form_response(dict_req)
			response = "{:.2f}".format(response)
			return render_template("Result.html",response=response)
	else:
		return render_template('Home.html')


if __name__ == "__main__":
	app.run()