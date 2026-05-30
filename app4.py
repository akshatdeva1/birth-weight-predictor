from flask import Flask, request, render_template
import pandas as pd
import pickle

app = Flask(__name__)

# Extract and clean the data from the form
def get_cleaned_data(form_data):

    gestation = float(form_data['gestation'])
    parity = float(form_data['parity'])
    age = float(form_data['age'])
    height = float(form_data['height'])
    weight = float(form_data['weight'])
    smoke = int(form_data['smoke'])

    cleaned_data = {
        "gestation": [gestation],
        "parity": [parity],
        "age": [age],
        "height": [height],
        "weight": [weight],
        "smoke": [smoke]
    }

    return cleaned_data


@app.route('/')
def home():
    return render_template("index1.html")


@app.route("/predict", methods=['POST'])
def get_prediction():

    # get data from form
    baby_data_form = request.form

    # clean data
    baby_data_cleaned = get_cleaned_data(baby_data_form)

    # create dataframe
    baby_df = pd.DataFrame(baby_data_cleaned)

    # load model
    with open("model/model.pkl", "rb") as obj:
        model = pickle.load(obj)

    # prediction
    prediction = model.predict(baby_df)
    prediction = round(float(prediction[0]), 2)

    return render_template(
        "index1.html",
        prediction=prediction
    )


if __name__ == '__main__':
    app.run(debug=True)