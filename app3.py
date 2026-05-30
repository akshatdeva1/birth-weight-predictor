from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Home Route
@app.route('/', methods=['GET'])
def home():
    return render_template('form1.html')


# Upload Route
@app.route('/upload', methods=['POST'])
def get_data():

    file = request.files['file']

    print("This is the name of the file:", request.files)
    print("File:", file)

    # Check CSV file
    if file.filename.endswith('.csv'):

        # Save file
        path = "userfile/" + file.filename
        file.save(path)

        # Read CSV file
        df = pd.read_csv(path)

        print(df.head())

        # Basic statistics
        min_salary = float(df['salary'].min())
        max_salary = float(df['salary'].max())
        total_employees = int(df['salary'].count())
        average_salary = float(df['salary'].mean())

        response = {
            "min_salary": min_salary,
            "max_salary": max_salary,
            "total_employees": total_employees,
            "average_salary": average_salary
        }

        return jsonify(response)

    else:
        return "Upload a CSV file only."


# Run Flask App
if __name__ == '__main__':
    app.run(debug=True)