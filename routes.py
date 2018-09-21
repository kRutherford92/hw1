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
        store = request.form.get('store')

        # one-hot encode categorical variables
        
        # Store
        for i in range(1115):
            if (i != 291) & (i != 622) & (i != 879):
                if i == store:
                    entered_li.append(1)
                else:
                    entered_li.append(0)

        # StoreType
        if store_type == 1:
            StoreType_a = 1
        else:
            StoreType_a = 0
        if store_type == 2:
            StoreType_b = 1
        else:
            StoreType_b = 0;
        if store_type == 3:
            StoreType_c = 1
        else:
            StoreType_c = 0
        if store_type == 4:
            StoreType_d = 1
        else:
            StoreType_d = 0

        # Assortment
        if assortment == 1:
            Assortment_a = 1
        else:
            Assortment_a = 0
        if assortment == 2:
            Assortment_b = 1
        else:
            Assortment_b = 0
        if assortment == 3:
            Assortment_c = 1
        else:
            Assortment_c = 0

        # State Holiday
        if state_holiday == 1:
            StateHoliday_0 = 1
        else:
            StateHoliday_0 = 0
        if state_holiday == 2:
            StateHoliday_a = 1
        else:
            StateHoliday_a = 0
        if state_holiday == 3:
            StateHoliday_b = 1
        else:
            StateHoliday_b = 0
        if state_holiday == 4:
            StateHoliday_c = 1
        else:
            StateHoliday_c = 0

        # manually specify competition distance
        comp_dist = 5458.1


        # build 1 observation for prediction
        
        entered_li.append(StoreType_a)
        entered_li.append(StoreType_b)
        entered_li.append(StoreType_c)
        entered_li.append(StoreType_d)
        entered_li.append(Assortment_a)
        entered_li.append(Assortment_b)
        entered_li.append(Assortment_c)
        entered_li.append(StateHoliday_0)
        entered_li.append(StateHoliday_a)
        entered_li.append(StateHoliday_b)
        entered_li.append(StateHoliday_c)
        entered_li.append(comp_dist)
        entered_li.append(promo2)
        entered_li.append(promo)
        entered_li.append(day_of_the_week)
        entered_li.append(month)
        entered_li.append(school_holiday)

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
