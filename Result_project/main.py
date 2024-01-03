from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<float:score>')
def success(score):
    result = "PASS" if score >= 50 else "FAIL"
    return render_template('result.html', result=result)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c_programming = float(request.form['cProgramming'])
        total_score = (science + maths + c_programming) / 3

    res = "success" if total_score >= 50 else "failed"
    return redirect(url_for('success', score=total_score))


@app.route('/form')
def show_form():
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
