from flask import Flask, render_template, request
from main import calculateBMI, getCategory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    heightFeet = int(request.form['heightFeet'])
    heightInches = int(request.form['heightInches'])
    weightPounds = int(request.form['weightPounds'])

    bmi = calculateBMI(heightFeet, heightInches, weightPounds)
    category = getCategory(bmi)

    return render_template('result.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)