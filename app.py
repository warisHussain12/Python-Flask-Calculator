import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method=='POST':
        firstInput = request.form['firstInput']
        secondInput = request.form['secondInput']
        result = int(firstInput) + int(secondInput)
        return render_template('index.html', result=result)
    return render_template('index.html')
    
if __name__ == '__main__':
    # app.run(debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
