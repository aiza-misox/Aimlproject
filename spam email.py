from flask import Flask,request,render_template,jsonify
import pickle
import numpy as np
app=Flask(__name__)
with open('email.pkl','rb') as file:
     model=pickle.load(file)
@app.route('/') 

def home():
    return render_template('ml.html')
@app.route('/predict',methods=['GET','POST'])
def predict():
    prediction_label = None
    if request.method == 'POST':
        try:
            email_text=request.form.get('email_text')
            print(email_text)
            prediction=model.predict(email_text)
            prediction_label='Spam'if prediction[0]==1 else 'Not Spam'
        except Exception as e:
            prediction = "Error in input data. Please check your values."
    return render_template('ml.html',{'prediction':prediction_label})
if __name__ == '_main_':
    app.run(debug=True)