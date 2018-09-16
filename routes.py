import flask
from flask import Flask, request, render_template
from sklearn.externals import joblib
import numpy as np

from utils import onehotCategorical

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return flask.render_template('index.html')


@app.route('/predict', methods=['POST'])
def make_prediction():
    if request.method=='POST':

        entered_li = []

        # ========== Part 2.3 ==========
        # YOUR CODE START HERE


        # get request values


        # one-hot encode categorical variables


        # manually specify competition distance
        comp_dist = 5458.1


        # build 1 observation for prediction


        # ========== End of Part 2.3 ==========

        # make prediction
        prediction = model.predict(np.array(entered_li).reshape(1, -1))
        label = str(np.squeeze(prediction.round(2)))

        return render_template('index.html', label=label)

if __name__ == '__main__':
    # load ML model
    # ========== Part 2.2 ==========
    # YOUR CODE START HERE

    # ========== End of Part 2.2 ==========
    # start API
    app.run(host='127.0.0.1', port=8000, debug=True)
