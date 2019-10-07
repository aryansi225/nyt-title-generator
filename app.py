from flask import Flask, render_template, request
from predictor import predict, get_model

app = Flask(__name__)

get_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result',methods=["POST"])
def output():
    if request.method == 'POST':
        seed = request.form['data']
        quantity = request.form['quantity']
        seed, quantity, predictions = predict(seed, quantity)
        return render_template('index.html', hasOutput = True, seed = seed, quantity = quantity, predictions = "\" "+predictions+" \"")
    
if __name__=='__main__':
    app.run(debug=False, threaded=False)