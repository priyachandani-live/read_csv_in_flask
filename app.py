import csv

from flask import (
    Flask, 
    render_template,
)

#Creating a flask instance
app = Flask(__name__)

#Local host route
@app.route('/')
def greeting():
    return "Welcome to our CSV Reader!"

#route to read csv
@app.route('/csv')
def read_csv():
    with open('static/test.csv', 'r') as file:
        csv_data = list(csv.reader(file))
        # print(csv.reader(file))
        # print(csv_data)
        # # for i in csv_data:
        # #     print(i)
        # #     for j in i:
        # #         print("JJJJ", j)
    return render_template('csv_template.html', data=csv_data)

if __name__ == '__main__':
    app.run()