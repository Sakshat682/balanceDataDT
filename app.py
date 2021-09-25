from flask import Flask, render_template, request
import pickle

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
        # LT = LW*LD
        # RT = RW*RD
        # classification=model.predict([[LT,RT]])
        classification=model.predict([[LW,LD,RW,RD]])
        output=classification[0]
        if output=='R':
            return render_template('index.html',classification_text="Right side is more heavy")
        elif output=='L':
            return render_template('index.html',classification_text="Left side is more heavy")
        elif output=='B':
            return render_template('index.html',classification_text="It is balanced")
        return render_template('index.html',classification_text="Not valid Output")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

