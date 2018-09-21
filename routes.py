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
        month = request.form.get('month')
        day_of_the_week = request.form.get('day_of_the_week')
        promo = request.form.get('promo')
        promo2 = request.form.get('promo2')
        state_holiday = request.form.get('state_holiday')
        school_holiday = request.form.get('school_holiday')
        assortment = request.form.get('assortment')
        store_type = request.form.get('store_type')

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
    model = joblib.load('rm.pkl')
    # ========== End of Part 2.2 ==========
    # start API
    app.run(host='127.0.0.1', port=8000, debug=True)
