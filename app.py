from flask import Flask, render_template, request
# import jsonify
# import requests
import pickle
# import numpy as np
import sklearn
app = Flask(__name__)
model = pickle.load(open('decision_trees_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/classify", methods=['POST'])
def classify():
    if request.method == 'POST':
        if not request.form.get('LW'):
            return render_template('index.html',classification_text="Please Enter Valid Left Weight")
        else:
            LW = int(request.form['LW'])
        if not request.form.get('LD'):
            return render_template('index.html',classification_text="Please Enter Valid Left Distance")
        else:
            LD = int(request.form['LD'])
        if not request.form.get('RW'):
            return render_template('index.html',classification_text="Please Enter Valid Right Weight")
        else:
           RW = int(request.form['RW'])
        if not request.form.get('RD'):
            return render_template('index.html',classification_text="Please Enter Valid Right Distance")
        else:
            RD = int(request.form['RD'])
        LT = LW*LD
        RT = RW*RD
        classification=model.predict([[LT,RT]])
        output=classification[0]
        if output==2:
            return render_template('index.html',classification_text="Right side is more heavy")
        elif output==1:
            return render_template('index.html',classification_text="Left side is more heavy")
        elif output==0:
            return render_template('index.html',classification_text="It is balanced")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

